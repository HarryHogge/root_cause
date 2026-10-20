# network_timeout_analysis.md

Attachment 65006, text, 12 KB, added 2026-09-30 by Scott Hunter.

# NIC_MAX_BLOCKING_TIME — Impact Evaluation

Evaluates the proposed fix in [xcomm_comms_freeze_summary.md](xcomm_comms_freeze_summary.md) against the actual `autopilot_202_40` and `xcomm_202_40` source. Both projects share nearly identical CycloneTCP network stacks and were evaluated in parallel.

## Scope of the Change

**Literal diff:** add `#define NIC_MAX_BLOCKING_TIME 200` to each project's `net_config.h`. Neither currently overrides it, so both inherit `INFINITE_DELAY` from `nic.h:34` today:
- `autopilot_202_40/Cyclone/net_config.h`
- `xcomm_202_40/Cyclone/net_config.h`

**Single code call site affected:** `osWaitForEvent(&interface->nicTxEvent, NIC_MAX_BLOCKING_TIME)` inside `nicSendPacket()` — `autopilot_202_40/Cyclone/cyclone_tcp/core/nic.c:299` (xcomm: `nic.c:298`, identical). Nothing else in CycloneTCP changes.

**Why that one site matters so much:** `NET_INTERFACE_COUNT` is `1` in both projects — one Ethernet interface, one `nicTxEvent`, one `netMutex` per board. `nicSendPacket()` has exactly 3 reachable callers:
- `ethernet.c:556` (`547` in xcomm) — path for **all** IP-over-Ethernet traffic (TCP, UDP, ARP-resolved sends)
- `ipv4.c:1061` — loopback-interface path, **dead code** in both (`NET_LOOPBACK_IF_SUPPORT` is `DISABLED` in both, `net.h:79`)
- `raw_socket.c:736` — only reachable in **xcomm** (`RAW_SOCKET_SUPPORT ENABLED` there, `DISABLED` in autopilot), used by `ping.c`'s ICMP raw-socket client

**Breadth of impact:** `netMutex` is acquired (blocking, no timeout) by nearly every CycloneTCP module — `net.c`, `socket.c`, `bsd_socket.c`, `ip.c`, `ipv4.c`, `tcp.c`, `tcp_misc.c`, `udp.c`, `raw_socket.c`, `ping.c`, `dhcp_client.c`, `dhcp_server.c`, `dns_client.c`, `dns_sd.c`, `auto_ip.c`, `llmnr_client.c`, `mdns_client.c`, `mdns_responder.c`, `mqtt_client_transport.c`, `nbns_client.c`, `snmp_agent_misc.c`, `web_socket.c`. Any task using any of these (HTTP/FTP servers, DHCP, mDNS, DNS, XComm's serial-out-over-UDP task, etc.) is blocked for as long as one task holds `netMutex` stuck in `nicSendPacket()` — consistent with the TRACE-delta evidence in the freeze summary. Bounding the wait shrinks that window from "forever" to the configured value for every one of those consumers, on both boards.

## Are the Timeouts Properly Handled?

**The drop path itself:** on timeout, `nic.c` sets `error = NO_ERROR` and returns without ever calling the driver's `sendPacket()` (`nic.c:315-318`). The packet is silently dropped and reported as success.

- **Buffer lifecycle:** `raw_socket.c` unconditionally frees the buffer right after the call regardless of error (`raw_socket.c:736-740`). `ethernet.c`/`ipv4.c` just propagate `error` to the caller — the same pre-existing contract used for any other `nicSendPacket` error (e.g. `ERROR_INVALID_INTERFACE`), so this introduces no new leak risk.
- **Protocol-level consistency:** TCP relies on peer ACKs/retransmission timers, not on `nicSendPacket`'s return value, to detect loss; UDP is inherently unreliable. A silent drop reported as `NO_ERROR` is indistinguishable from a real Ethernet-level drop the upper layers must already tolerate — not a new failure class.
- **No new concurrency risk:** on timeout, `disableIrq`/`sendPacket`/`enableIrq` are simply skipped entirely — no partial/racy hardware access introduced.

**Critical gap — bounding the wait alone does NOT restore TX capability.** `nicSendPacket()` will keep hitting the same un-signaled `nicTxEvent` on every subsequent call (the EMAC TX DMA is still stalled), timing out and dropping **every** outbound Ethernet packet indefinitely until the hardware is actually recovered. Checked both `pic32mz_eth_driver.c` files — the "defense-in-depth" EMAC TX-stall recovery described in the freeze summary **does not exist in either project**. `pic32mzEthTick()` currently only polls the PHY/switch driver (`xcomm_202_40/.../pic32mz_eth_driver.c:353-368`); there is no `ETHCON1CLR`/TXRTS-abort/descriptor-reclaim code anywhere, and the `g_inject_txstall` bench test referenced in the summary doesn't exist in this codebase either.

**Consequence if only the one-line define is applied:** the board stops deadlocking (other tasks resume), but Ethernet egress goes silently and permanently dark after any real stall — no watchdog trip, no automatic recovery. That is arguably **worse** than the current T95_V515 behavior (repeated WDT reboots that do restore comms automatically every few minutes), though better than the vehicle-863 freeze case (which required a physical power cycle). **The one-line fix must not ship without the EMAC recovery code.**

**Dependency ordering (non-obvious):** `netTick()`/`pic32mzEthTick()` only runs inside `netTask()`'s own `osAcquireMutex(&netMutex)` section (`net.c:1265-1400`). Today, while a TX-stalled task holds `netMutex` blocked forever inside `nicSendPacket()`, `netTask` can never acquire `netMutex` to run `netTick()` at all. This means the bounded-wait fix is a **hard prerequisite** for the EMAC recovery fix to ever execute — without it, any future recovery code placed in `pic32mzEthTick()` is unreachable exactly when it's needed. Both changes must land together.

## Symmetry Between Projects

`nic.c`, `nic.h`, `net.c`, and the netMutex/netTick architecture are byte-for-byte identical between `autopilot_202_40` and `xcomm_202_40`. Both currently default to `INFINITE_DELAY` and both are equally exposed. The fix (config define + driver recovery code) must be applied to **both** `net_config.h` files and **both** `pic32mz_eth_driver.c` files, or one board remains fully exposed to the freeze.

One divergence worth noting: xcomm has `RAW_SOCKET_SUPPORT ENABLED` (used by `ping.c` for ICMP echo), exercising the same `nicSendPacket` choke point via a second call path; autopilot has it `DISABLED` so that path is compiled out there. Not a blocker for the fix — just an extra active producer sharing the same bottleneck on xcomm.

## Recommendation Before Committing

- Apply `NIC_MAX_BLOCKING_TIME` **together with** the `pic32mzEthTick()` EMAC recovery code in both projects — never one without the other.
- Validate the `200` ms value empirically (bench TX-stall injection — referenced but not present in this codebase — plus a legitimate max-load soak test) rather than treating it as self-evidently correct. `NIC_TICK_INTERVAL`/`NET_TICK_INTERVAL` are both 1000 ms, so recovery latency and the drop-timeout value interact, but there's no existing bench data in this codebase confirming 200 ms is both long enough to avoid dropping healthy-but-momentarily-busy sends and short enough to keep the freeze window acceptable.

## Driver-Level Recovery Proposal (not applied)

`nicTxEvent` is only ever set from two places in the driver, both requiring hardware progress a stall prevents:
- `pic32mzEthIrqHandler()` on `TXDONE`, gated on `txCurBufferDesc->control & ETH_TX_CTRL_EOWN == 0` — `xcomm_202_40/.../pic32mz_eth_driver.c:454-459`
- `pic32mzEthSendPacket()`, immediately, only if the next descriptor is already free — `pic32mz_eth_driver.c:563-566`

During a real stall neither fires, so recovery **must be periodic/polling** — there is no event to hook when the failure mode is the absence of an event.

**Proposed change — `pic32mz_eth_driver.c:353-368`** (identical in both projects). `pic32mzEthTick()` already runs once per `NIC_TICK_INTERVAL` (1000 ms) from `netTick()`, which always holds `netMutex` (`net.c:1394-1399`) — the same mutex `nicSendPacket()` holds while stuck, so this is naturally serialized with no new locking needed. It also only becomes reachable once `NIC_MAX_BLOCKING_TIME` is bounded, since otherwise the stuck task never releases `netMutex` for `netTick()` to run at all.

```c
// old
void pic32mzEthTick(NetInterface *interface)
{
   if(interface->phyDriver != NULL)
      interface->phyDriver->tick(interface);
   else if(interface->switchDriver != NULL)
      interface->switchDriver->tick(interface);
}
```

```c
// new
static uint_t txStallTickCount = 0;

void pic32mzEthTick(NetInterface *interface)
{
   uint_t i;

   //TX descriptor still owned by the DMA?
   if((txCurBufferDesc->control & ETH_TX_CTRL_EOWN) != 0)
   {
      txStallTickCount++;
      //No progress for 2 consecutive ticks (~2s) -> declare a TX stall
      if(txStallTickCount >= 2)
      {
         ETHCON1CLR = _ETHCON1_TXRTS_MASK;                  //abort the stuck TX engine
         for(i = 0; i < PIC32MZ_ETH_TX_BUFFER_COUNT; i++)
            txBufferDesc[i].control &= ~ETH_TX_CTRL_EOWN;   //reclaim every descriptor
         ETHTXST = KVA_TO_PA(&txBufferDesc[0]);              //reset TX pointer
         txCurBufferDesc = &txBufferDesc[0];                 //resync software pointer (missing from the original doc snippet)
         osSetEvent(&interface->nicTxEvent);                 //unblock any waiter
         txStallTickCount = 0;
      }
   }
   else
   {
      txStallTickCount = 0;
   }

   if(interface->phyDriver != NULL)
      interface->phyDriver->tick(interface);
   else if(interface->switchDriver != NULL)
      interface->switchDriver->tick(interface);
}
```

Gap versus the original doc snippet: it reset `ETHTXST` but never resynced the driver's own `txCurBufferDesc` software pointer back to `&txBufferDesc[0]`. Without that, `pic32mzEthSendPacket()` would keep writing to whatever descriptor it was already pointing at, out of sync with where hardware now expects to read from. Added above.

Threshold (2 ticks / ~2s) is a judgment call, not bench-validated — should be checked against real max legitimate TX latency before committing.

**Not applied to source** — proposal only, per review constraints.

## Application-Level Alternative (also not applied)

Investigated whether recovery could be done entirely in application code, avoiding any `Cyclone/` file changes.

**Detection can be fully application-level:** a heartbeat pattern — two `volatile` timestamps set by the sending code around its `socketSendTo()` call (one before the call, one after it returns successfully), checked by a periodic 1Hz/10Hz task (e.g. the existing `OneHz` task already present in both projects) for staleness.

**Recovery cannot be purely application-level.** Every public CycloneTCP entry point that could serve as a runtime recovery action shares the same unbounded `netMutex` the stuck task is holding:
- `netConfigInterface()` — `xcomm_202_40/.../net.c:936-941` — fully reinitializes the driver, but calls `osAcquireMutex(&netMutex)` first
- `netSetLinkState()` — `net.c:878-888` — same prerequisite

A watchdog task calling either would simply block forever alongside every other task. FreeRTOS provides no mechanism to force a task out of an indefinite mutex-take/event-wait from outside, and deleting the stuck task would orphan `netMutex` permanently (worse than the original freeze). **A bounded wait must exist somewhere inside the blocking chain before any recovery action — app-level or not — can run.**

That said, `NIC_MAX_BLOCKING_TIME` is CycloneTCP's own documented override point (`nic.h:33-36`, `#ifndef` pattern) set from the project-owned `net_config.h`, not vendor source under `cyclone_tcp/` — so it's a config value, not a "network stack modification" in the sense of touching vendor `.c` files.

Once that one config value is bounded, detection and recovery can both live in application code:
- **Detection:** heartbeat pattern described above.
- **Recovery:** call the existing public `netConfigInterface()` from the watchdog task instead of hand-rolled register pokes — reuses the already-tested init path, zero new stack code.

**Caveat:** `netConfigInterface()` is currently only called once, at boot, in `WebServer.c:463`/`445`, immediately followed by static-IP or `dhcpClientStart()` calls (`WebServer.c:510,542`). It does not restore IP configuration by itself — calling it at runtime without also replaying that IP-assignment logic would leave the interface reinitialized but address-less. That replay logic would need to be factored out and re-invoked by the watchdog too.

**Net conclusion:** one unavoidable config-file line in `net_config.h`, plus a fully application-level 1Hz/10Hz watchdog task (heartbeat detection + `netConfigInterface()` + IP re-assignment) for the rest.
