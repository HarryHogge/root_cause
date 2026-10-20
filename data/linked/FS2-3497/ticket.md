# FS2-3497: XComm Fuel Cell GBurn is reset during fuel cell starts

- **Issue type:** Bug
- **Status:** To Do
- **Priority:** High
- **Created:** 2025-07-23
- **Updated:** 2026-09-04
- **Reporter:** Jason Scherer
- **Assignee:** Jason Scherer
- **Creator:** Jason Scherer
- **Links:** relates to MS-800 (VSM: Implement workaround for Fuel Cell remaining fuel when restarted in flight); relates to VXEP-1513 (VXE-378 Fuel cell errors (overheating) and unable to maintain charge on HLB)
- **Sprint:** FS2 Sprint 40, FS2 Sprint 34
- **Impacted HW Version(s):** BLK30_Adv_Nav, BLK30_Std

## Description

Ok, I have reviewed the XComm and GCS code with the assistance of Copilot and Grok. The issue seems to be two fold. 1.) The XComm resets 'gburn_accum' to 0 during starts instead of only on initialization. 2.) The GCS doesn't take advantage of the 0x8001 message which has the XComm calculated cumulative burn, so the xcomm reset of gburn_accum causes the value to jump back to initial fuel level. 
 
Good news is that we can fix this in either XComm or GCS or both would be best. So pick your poison. 
 
Here is the summary of the issue from Grok
 
Copilot's investigation into the GCS code is accurate and aligns well with the behavior we've been discussing. It confirms the root cause: the GCS calculates remaining fuel using the GBurn field from the AMI packet (which resets on restart due to the gburn_accum = 0 in XComm's Poll() case 2), and it completely ignores the 0x8001 short status message (pre-computed remaining fuel). This leads to the display jumping back to the initial value after a restart.
To verify this independently, I simulated key parts of the GCS code (from FuelCellControl.cpp and the Vehicle.cpp short status handling) using a code execution tool. The output matches expectations:
- Initial setup (0x8000 sets initial to 800): Remaining = 800.0
- After burn (AMI packet sets GBurn=25): Remaining = 775.0
- After restart (AMI packet with GBurn=0): Remaining = 800.0 (jump back)
- Processing 0x8001 (remaining=775): Ignored, so remaining stays at 800.0
- Simulated fix (using 0x8001 to adjust): Remaining = 775.0 (persists correctly)

This proves the GCS relies solely on the AMI packet's GBurn for the calculation, and the lack of 0x8001 handling prevents using XComm's cumulative remaining value.
**Why This Happens in GCS Code**

- Remaining Fuel Calculation: In FuelCellControl.cpp (line ~814), GetRemainingFuel() explicitly uses GetInitialFuel() - (double) m_state.GBurn. m_state.GBurn is updated via SetState() from the AMI packet (processed in Protocol.cpp ~line 1030: memmove(&state, RxBuf, sizeof(state)); fuelcelldlg->SetState(state);).
- Short Status Handling: In Vehicle.cpp (lines ~5446-5475), 0x8000 sets initial fuel (fuelcelldlg->SetInitialFuel(sst->Parm2);), but 0x8001 has no code—just a comment ("// what's left in parm2 // *** NO IMPLEMENTATION! ***"). So it's ignored, bypassing the persistent remaining fuel.
- Display Update: In FuelCellControl.cpp (line ~351), the "Grams Remain" gauge is set with m_burn.SetPositionNoEvent(remain); where remain = m_InitialFuelGrams - (double) state.GBurn—again, tied to GBurn from AMI.
- No Use of Burned Field: The GCS doesn't use state.Burned (FC hardware-reported burn) for remaining calculations—it's all GBurn (software-derived). If the FC resets Burned per-run, it wouldn't help anyway, but the code doesn't reference it for this purpose.

The mismatch is clear: GCS expects cumulative burn but gets a reset value from AMI after restart, and skips the direct fix (0x8001).
**Recommendations/Fixes**

Since the issue spans XComm (reset) and GCS (ignoring 0x8001, relying on reset-prone GBurn), fix both for robustness. Prioritize based on your codebase access.
- Fix in XComm (Prevents Reset – Recommended First):
- In FuelCell.cpp CFuelCell::Poll() case 2: Remove gburn_accum = 0;. This keeps cumulative burn across restarts (only reset on boot/refuel via fcSetInitFuel()).
- Add a check: if (!m_wasrunning) gburn_accum = 0; (reset only if not a hot restart).
- Test: Simulate burn → stop → start; verify GBurn persists in AMI packets.
- Impact: Fixes root cause; GCS display won't jump since GBurn won't reset.
- Fix in GCS (Use Ignored 0x8001 – Quick Win):
- In Vehicle.cpp ~line 5465 (under else if((sst->Parm1 & 0xffff) == 0x8001)): Add fuelcelldlg->SetRemainingFuel(sst->Parm2);.
- Add to FuelCellControl.h/cpp: void SetRemainingFuel(double remaining) { m_remainingFuel = remaining; } (new member double m_remainingFuel; initialized to m_InitialFuelGrams).
- Update GetRemainingFuel(): return m_remainingFuel; (bypass GBurn calc).
- Update gauge in UpdateDisplay(): Use m_remainingFuel instead of recalculating.
- Test: Send 0x8001 with remaining=775 after restart; verify display uses it.
- Impact: GCS uses XComm's pre-computed cumulative remaining, ignoring AMI resets.
- Alternative: GCS Tracks Independently:
- In FuelCellControl.cpp, add a persistent double m_cumulativeGBurn = 0.0;.
- In SetState(): m_cumulativeGBurn = max(m_cumulativeGBurn, (double)state.GBurn); (accumulate max to handle resets).
- Update GetRemainingFuel(): Use m_InitialFuelGrams - m_cumulativeGBurn.
- Drawback: More complex; assumes GBurn only increases (true unless errors).
- Enhancements:
- Log AMI/short status around restarts for debugging (add to SetState() and short status handler).
- If FC hardware Burned is cumulative, switch GCS to use it instead of GBurn (update GetRemainingFuel() to - (double)m_state.Burned).
- UI: Add warning if remaining jumps > threshold (detect restart artifact).

Implement #1 and #2 for full fix. If you provide patches or more code, I can refine simulations!

## Comments (0)

## Attachments (0)
