# FS2-4207: XCOMM: 4.75_rc3 reset investigation

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2026-01-22
- **Updated:** 2026-04-13
- **Resolved:** 2026-04-13
- **Reporter:** Scott Hunter
- **Assignee:** Scott Hunter
- **Creator:** Scott Hunter
- **Parent:** FS2-4309 B40 WD Investigation
- **Links:** relates to VXEP-1692 (B40/30 XCOM WDT resets )
- **Epic Link:** FS2-4309
- **Sprint:** FS2 Sprint 37, FS2 Sprint 36

## Description

A ticket to coordinate investigation of exceptions observed in XComm version 4.75_rc3
FYI, @David Grosher @Scott Whitney

## Comments (10)

### Scott Hunter, 2026-01-22

Steps 
Generate a build where the tasks aren't startedBeeperUser IO? (Switch Control)StatusTextAnalogCaptureHobbsHTTP Conn [1-4]UDP:50100UDP5005XComm Geo/KXComm PingGet that build running on hardwareGet the optional web page start goingGet that build running on hardwareGet to the bottom of what we've seen or not seen in the past with stack overflow based on my new understandingGenerate code that will overflow stack on command and see what the crash dumps showGet to the bottom of what’s gone wrong with the switched-in dumps being out of order

### Scott Hunter, 2026-01-22

Previous attempt resulted in boot loops, Going to restore some of the tasks
Don’t start these
BeeperStatusTextHTTP Conn [1-4]UDP:50100UDP5005Add Back
User IO? (Switch Control)AnalogCaptureHobbsXComm Geo/KXComm Ping

### Scott Hunter, 2026-01-23

Today I got the DKT-01 system mostly back to operating as a mini iron bird and made some progress eliminating tasks after the previous attempt for deleting everything failed. The DKT-01 setup still needs the correct gcs.ini entry to make it through the launch wizard without GPS and it’d be nice for testing if a reboot of the VTOL wasn’t required. The settings I thought were correct are not working today.
The most important thing I learned was that not starting the web tasks won’t work in XComm the way it did during my investigation last year working with the VTOL. The XComm is much more dependent on the network and the system depends on XComm’s network.
I was able to get two builds lightly tested. First is a build that doesn’t start the Hobbs (aka maintenance) task, the other adds sensorCapture to the list of tasks that aren’t started. The sensorCapture version keeps the init calls so the “getters” return their initial value of 0.
Both of these builds seem to work and are able to progress through the launch wizard up until the GPS is required. Servos move, battery pages are what I expect and other spot checks look o.k.
I do see “X: Bus Fault 67” in the GCS debug window at about 1Hz, I need to track that down. Bus Fault is from the removal of sensorCapture.
@Scott Whitney @David Grosher

### Scott Hunter, 2026-01-24

Starting off by changing the number of http connections to 1, from 4.  I expected to only be able to have one active web page at a time open but that’s not the case. Multiple live pages can be served in this config. A “connection” must mean how many external clients are in use? Note: This seems to free up 10-15K of heap

### Scott Hunter, 2026-01-24

XComm is acting up, the XComm isn’t booting and APBL is unable to complete the process of reflashing.

### Scott Hunter, 2026-01-25

I’m back in on XComm#407! Something is taking a very long time during the program step from APBL.exe. This happened with the RC3 release of XComm so it shouldn’t have anything to do with the changes I’m making.

Note: Free heap when the first TRACE table is dumped:
- RC3 36,864
- 1 HTTP server, no sensor cap, no Hobbs 53,248
- 2 HTTP server, no sensor cap, no Hobbs 49,152

### Scott Hunter, 2026-01-25

With the http server count at 1, we can’t reload from the web page. Claude says this is expected:
The Issue with maxConnections = 1
With only 1 connection:
User uploads firmware → Connection 1 is locked handling the POST
Browser tries to poll progress.xml → Blocked! No available connection
Progress monitoring fails
Timeout or hang likely occurs
Why Everything Else Works with 1 Connection
Normal web browsing:
Load page → connection closes → load next page → connection closes
Sequential, not simultaneous
Flash operation:
Upload POST stays open during programming
AJAX progress poll needs second connection simultaneously
Bottom line: Keep APP_HTTP_MAX_CONNECTIONS at 2 (or higher) to support the simultaneous upload + progress monitoring pattern used during firmware updates.

### Scott Hunter, 2026-01-25

With beeper removed, LW is still o.k. Free heap here is 53248. So it’s looking like ~4K per task?

### Scott Hunter, 2026-01-25

I added the code to capture stack pointer and return address then did a test with a null pointer instead of while(1) for the utility func to WD Reset.
- crash diag[5]: 800476d0 (stack pointer) - 
- From the map file - stack 0x8007ad88 0x5170 20848  Reserved for stack
- This is in the heap
- To understand what the stack pointer means we’d need to call the code below to capture the stack for each task
- TaskHandle_t handle = xTaskGetHandle("sensorcap");
- StackType_t* stackBase = pxTaskGetStackStart(handle); // If you have this API
- crash diag[6]: 9d1058ac (return address) - xc32-addr2line doesn’t know and the map file points to “simple_tlb_refill_context” from libpic32.a(simple-tlb-refill-exception.o)

The code captured the dump below:
[21:54:30.148 1.148] WD BOOT 16
[21:54:30.148 1.148] Index 0
[21:54:30.150 1.150] diag0 153
[21:54:30.150 1.150] diag1 0
[21:54:30.150 1.150] diag2 0
[21:54:30.152 1.152] diag3 0
[21:54:30.152 1.152] diag4 0
[21:54:30.152 1.154] diag5 0
[21:54:30.154 1.154] diag6 0
[21:54:30.154 1.154] diag7 0
** crash restart dump **
Crash@: 800312c4 0000ffff
reset reason: 00000010 : WDT
nmi reason: 00000000
crash addr: 9d11c1e4
crash diag[0]: 00000003
crash diag[1]: 00000000
crash diag[2]: 00000000
crash diag[3]: 00000000
crash diag[4]: 00000099
crash diag[5]: 800476d0
crash diag[6]: 9d1058ac
spare: 0

### Scott Hunter, 2026-01-26

Stubbed out analog readings to avoid log spamming and added the stack pointer for each task to the TCB-Name dump at startup

branch: FS2-4207-xcomm-4.75_rc3-reset-investigat
commit: 7da168521b3659098422c0c04cdb6c9eec84df53
tag: StubAnalogInPlusAddStackPointersToDump_LWOK

## Attachments (0)
