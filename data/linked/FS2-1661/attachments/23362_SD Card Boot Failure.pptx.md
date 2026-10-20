# SD Card Boot Failure.pptx

Attachment 23362, pptx, 297 KB, added 2024-09-24 by Kurt Burian.

## Slide 1

SD Card Boot Failure
9/23/2024

## Slide 2

Summary
XCOMM and VTOL AP will allow launch with a failed SD Card, provided the CPU can boot the operating system.
If a SD Card fails to initialize gracefully, for example failing to enter idle state, system will boot and display “Error Reading Directory” under drive status. Vehicle will still launch in this state.
If a SD Card triggers initialization timeout code, access violations will result in watch dog resets. The vehicle cannot be launched in this state.

## Slide 3

File System Startup
Each drive number loaded, 5 retry attempts each:
0: ROM
1: SD
2: FLASH
fsInit(<Drive Number>) calls the initialization routine for each driver.
// install file system handler vectors
wdtClear();
romInstall(); // file system stored in program memory
wdtClear();
sdInstall(); // sd card
wdtClear();
flashInstall(); // serial flash
wdtClear();
filestreamInit();
TaskSetup(); // init the RTOS
// initialize the file system for the fixed drives
int tries = 5;

...

tries = 5;
while(tries)
{
    tries--;
    wdtClear();
    sd_okay = (fsInit(DRIVE_SD) == NO_ERROR) ? true : false;
    if(sd_okay)
        tries = 0;
}
...
if(sd_okay)
{
    wdtStop(); // is this a good idea?
    AddMessage("copying web data to sd card");
    fsCopyPath("0:", "sd1:/www", true); // copy rom file image to sd card
    fsCopyFile("0:/popstat.xml", "sd1:/www/temp/popstat.xml"); // make these work for the configuration pages
    fsCopyFile("0:/progress.xml", "sd1:/www/temp/progress.xml");
    wdtStart();
}
else
{
    AddMessage("SD Card fault, operating out of ROM image");
    // fallback to running from flash?
}
AddMessageInt("heap free before scheduler", HeapCheck());
wdtClear();
...
vTaskStartScheduler(); // should never return from this
XCOMM:main.cpp:main(void)

## Slide 4

SD Card Initialization Process
Initialization
Set CLK between 100-400 khz. DI and CS high and apply >74 CLK pulses to SCLK. Card enters operating mode ready for commands
Send CMD0 with CS low to reset the card. Card will respond R1 with idle bit set
Send CMD8 with 0x000001AA to determine. If fail v1 or mmc v3. If success v2+.
Send ACMD41 with HCS set to check for SDC support and to start the init process. 
Read OCR register with CMD58 to check voltage range and high capacity(SDHC/SDXC)
Change SPI CLK to the correct operating speed.
[picture]

## Slide 5

Bug - Access Violation - mmcPIC32.c
Original - sd_disk_initialize
Timer1 = 1000;                        /* Initialization timeout of 1000 msec */
….
while (Timer1 && send_cmd(ACMD41, 0x40000000)); /* Wait for leaving idle state (ACMD41 with HCS bit) */
Fix – sd_disk_initialize
long long Timer10 = ReadCoreTimerLongFast()+1000*10000;                     /* Initialization timeout of 1000 msec */
 ….
while (Timer10 - ReadCoreTimerLongFast() > 0 && send_cmd(ACMD41, 0x40000000)){
/*-----------------------------------------------------------------------*/
void sd_disk_timerproc (void)
{
……
    UINT n;
n = Timer1;                     /* 1000Hz decrement timer */
    if (n) Timer1 = --n;
n = Timer2;
    if (n) Timer2 = --n;
Original - sd_disk_timerproc
A corrupt SD Card causes the driver to utilize the timeouts in the initialization code. An access violation leads to a WDT timeout after ~2sec, however it is not logged because the taskScheduler has not yet started.
Using the CoreTimer avoids reading from Timer1 in the sd task while an interrupt writes to the same variable every ms.
We assume CoreTimer is safe to read without semaphores since its part of the low-level hardware.
Fix – wait_ready
long long Timer20 = ReadCoreTimerLongFast() + 500*10000;
    rcvr_spi();
   do{
        res = rcvr_spi();
 }while ((res != 0xFF) && (Timer20 - ReadCoreTimerLongFast() > 0));  // wait for ff reply or timeout
Original – wait_ready
Timer2 = 500;  /* Wait for ready in timeout of 500ms */
    rcvr_spi();
    do
        res = rcvr_spi();
    while ((res != 0xFF) && Timer2);    // wait for ff reply or timeout

## Slide 6

Backup SlideBug – Web Content Requires SD Drive
Only point web root to SD Drive if both drive successfully mount and config checksum matches. 

sd_okay set true if mount succeeds

If drive mounts, but cant be read, webpage will fail to load. 

Fix - configReadOk() returns true if flash checksum matches or sd config exists.
#define DRIVE_WWW_DIR "SD1:/www/“
#define DRIVE_WWW_DIR_ROM "ROM:/“
#define DRIVE_WWW_DIR_FLSH "FLSH:/www/“

Original

if(sd_okay)
{
	strcpy(httpServerSettings.rootDirectory, DRIVE_WWW_DIR);
}
else
{
	strcpy(httpServerSettings.rootDirectory, DRIVE_WWW_DIR_ROM); 
}
Fix

if(sd_okay && configReadOk())
{
	strcpy(httpServerSettings.rootDirectory, DRIVE_WWW_DIR);
}
else
{
	strcpy(httpServerSettings.rootDirectory, DRIVE_WWW_DIR_ROM); 
}
WebServer.c WebServerStart()

## Slide 7

Backup SlideBug – Flash Checksum Ignored
config_success = false;
bool read_old = true;
if(cfgflashHasConfig()) // if a valid config exists, load it
{
    AddMessage("flash config exists, read it");
    configLoadImage();
    if(cfgflashGetChecksum() == configGetAlertChecksum())
    {
        AddMessage("flash config checksum good");
        config_success = true;
    }
    else
    {
        AddMessage("flash config checksum bad");
    }
    read_old = !config_success;
    read_old = false; // test
}
else
{
    AddMessage("flash config not found");
}
if(read_old) // if not, load older config type
{
    AddMessage("no or invalid flash config, read from files");
    readactive = true;
    int i;
    bool readok = true;
    for(i = 0; i < configGetEntries(); i++)
    {
        ConfigRecord* rec = (ConfigRecord*) configGetItem(i);
        if(configIsRoot(rec))
        {
            bool try = configReadConfig(rec);
            if(!try)
            {
                AddMessage("try config read again");
                try = configReadConfig(rec);
            }
            readok = readok && try;
        }
    }

    readactive = false;
    config_success = readok;
    AddMessage("image saved from config read");
    configSaveImage();
}
