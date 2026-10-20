# jetson_serial_output.txt

Attachment 54307, text, 3 KB, added 2026-04-22 by Bethany Ponce.

Jetson MCM Serial Output — Boot Failure Transcript
====================================================
Captured via PuTTY Serial Console (/dev/ttyUSB)
====================================================

--- SECTION 1: MB2 / Secure Boot Chain ---

I> cpubl: Authentication Finalize Done
I> Binary cpubl loaded successfully at 0x46e600000
I> tos: Authentication Finalize Done
I> Binary tos loaded successfully at 0x47fdee000
I> Relocating OP-TEE dtb from: 0x47fefec50 to 0x47c000020, size: 0x2106
I> [0] START: 0x80000000, SIZE: 0x3eea70000
I> [1] START: 0x472000000, SIZE: 0x2000000
I> Setting NS memory ranges to OP-TEE dtb finished.
I> Partition name: A_eks
I> Size of partition: 262144
I> Binary@ device:3/0 block-44288 (partition size: 0x40000), name: A_eks
I> eks: Authentication Finalize Done
I> Binary eks loaded successfully at 0x470000200
I> EKB detected (length: 0x410) @ VA:0x470000200
I> Task: Prepare TOS params (0x500194f8)
I> Setting EKB blob info to OPTEE dtb finished.
I> Setting OPTEE arg3: 0x47c000020
I> Task: OEM SC7 context save (0x5001a88c)
I> OEM sc7 context saved
I> Task: Disable MSS perf stats (0x50027f00)
I> Task::Program display sticky bits (0x50027e7c)
I> Task: Storage device deinit (0x500020a0)
I> Task: SMMU external bypass disable (0x50017894)
I> Task: SMMU init (0x500177b0)
I> Task: Program GICv3 registers (0x50027fa0)
I> Task: Audit firewall settings (0x50024fbc)
I> Task: Bootchain failure check (0x500025e8)
I> Current Boot-Chain Slot: 0
I> BR-BCT Boot-Chain is 0, and status is 1. Set UPDATE_BRBCT bit to 0
I> MB2 finished

--- SECTION 2: BL31 / OP-TEE Init ---

NOTICE:  BL31: v2.6(release):346877e39
NOTICE:  BL31: Built : 12:32:40, Aug 1 2023
I/TC: Physical secure memory base 0x47c040000 size 0x3fc0000
I/TC:
I/TC: Non-secure external DT found
I/TC: OP-TEE version: 3.21 (gcc version 9.3.0 (Buildroot 2020.08)) #2 Tue Aug 1 19:39:55 UTC 2023 aarch64
I/TC: WARNING: This OP-TEE configuration might be insecure!
I/TC: WARNING: Please check https://optee.readthedocs.io/en/latest/architecture/porting_guidelines.html
I/TC: Primary CPU initializing
I/TC: Test OEM keys are being used. This is insecure for shipping products!
I/TC: Primary CPU switching to normal world boot

Jetson UEFI firmware (version 2022.10.3-52cefd4-dirty built on 2024-05-27T13:47:35+00:00)

--- SECTION 3: OP-TEE Shared Memory Configuration ---

I/TC: Reserved shared memory is disabled
I/TC: Dynamic shared memory is enabled
I/TC: Normal World virtualization support is disabled
I/TC: Asynchronous notifications are disabled

--- SECTION 4: FATAL ERROR — Boot Hang ---

E/TC:?? 00 get_rpc_alloc_res:645 RPC allocation failed. Non-secure world result: ret=0xffff0000 ret_origin=0
E/LD:   init_elf:486 sys_open_ta_bin(bc50d971-d4c9-42c4-82cb-343fb7f37896)
E/TC:?? 00 ldelf_init_with_ldelf:131 ldelf failed with res: 0xffff000c

--- END OF CAPTURED OUTPUT ---
-- Boot halts here. Linux normal world never reached. No login prompt. Network interfaces unresponsive. --
