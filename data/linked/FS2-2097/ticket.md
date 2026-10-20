# FS2-2097: VTOL - Mag fault logging

- **Issue type:** Bug
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-07-22
- **Updated:** 2024-10-15
- **Resolved:** 2024-10-15
- **Reporter:** Scott Hunter
- **Assignee:** Scott Hunter
- **Creator:** Scott Hunter
- **Links:** relates to FS2-2406 (VTOL: Log good->bad transition of mag fault every time, rather than just once.); relates to FS2-2407 (Evaluate resource hit for enabling floating-point support in all tasks.)
- **Sprint:** FS2 Sprint 25

## Description

During testing July 19, 2024 a mag fault was logged:
[12:55:27.001 343.002] MAGFAIL: ratio > [ratio, 1+margin, mag, erf] 2147483647  399  47841  0
This indicates:
- The ratio was 2147483647/1000.
- The expected field, erf, was 0. Or at least less than 1/1000.
- Before calculating the ratio, the erf value is checked for being >= .01
- This set of printout values is “impossible”

The ratio in this context is measured mag field divided by the expected magnetic field. The expected mag field is read from a file and stored in a local variable in CalcImuMagFieldOk(), the value isn’t vulnerable to an external task changing the value.
Speculation - AddMessage may not be handling things correctly, something may have corrupted the stack to change the erf value but the mag data value is reasonable.
Also, the code is displaying 1-margin rather than the indicated 1+margin. 
```
extern "C" void CalcImuMagFieldOk()
{
    static bool oneShot = true;
	if(hilIsActive())
    {
        imuMagFieldOkFlag = true;
		return;
    }
    
	static float mag = -1.0f;
	float erf = pvGetEarthMagStrength();
	if(mag == -1.0f)
		if(erf != 0.0f)		// wait for wmm magic
			mag = erf;		// and init the filtered mag to a reasonable value

	if(erf > 0.01f)
	{
		mag = (mag*5.0f + MagTotal) / 6.0f;
		
		float rat = mag / erf;		// filtered actual / predicted

		// updated 2/10/2022 to make the mag qualification less scalpel and more axe
    
		if(fabsf(erf - mag) < magdelta)	// compare the absolute difference against threshold
        {
            imuMagFieldOkFlag = true;
			return;
        }
		
		if(rat > (1.0f + magmargin))	// compare the ratio against threshold
        {
            imuMagFieldOkFlag = false;
            if ( oneShot )
            {
                oneShot = false;
                AddMessageInt4("MAGFAIL: ratio > [ratio, 1+margin, mag, erf]", (int)(1000*rat), (int)(1000 * (1.-magmargin)), (int)(1000*mag), (int)(1000*erf));
            }
			return;
        }
		if(rat < (1.0f - magmargin))
        {
            imuMagFieldOkFlag = false;
            if ( oneShot )
            {
                oneShot = false;
                AddMessageInt4("MAGFAIL: ratio < [ratio, 1-margin, mag, erf]", (int)(1000*rat), (int)(1000 * (1.-magmargin)), (int)(1000*mag), (int)(1000*erf));
            }
			return;
        }
	}
    imuMagFieldOkFlag = true;
	return;
}
```

## Comments (8)

### Scott Hunter, 2024-09-05

The same, or related, issue appears to have been captured in https://jenaero.atlassian.net/browse/VXEP-579?atlOrigin=eyJpIjoiMTFhNzU1YjA5NTEyNDc0MTk3YWQ0OWUxZTA1MjVhOWYiLCJwIjoiaiJ9 
In addition to the recommendations above, I think we should log each transition from good->bad in the mag field and transitions from bad->good in order to capture more data should this happen again. It would also improve our ability to diagnose this issue if we record the raw mag sensor readings for all 3 axes instead of just the magnitude. The data recorded in the CSV file has been transposed to account for the sensor installation, I’d like to see the raw data right from the sensor.

### Scott Hunter, 2024-10-02

FYI @David Grosher @Eric Brewer 
The attached AAR, T95_689_240930_145516_pack.zip, is from a MAGNSS flight where the magnetometer failed and healed. The logged fault indicates the measured magnetic field dropped below the allowable threshold. The recorded mag data in the AAR does not show anything close to a fault condition. The magnitude of the field at the time of the fault was .5, the field reported in the fault is 0.086.
I found the task that calculates MagTotal is running at 100Hz & priority=3 and the code that use MagTotal is running at 1Hz & priority=1.  It does seem like the processing protects against corruption of MagTotal though. It’s calculated in a local variable then copied to the output parameter
The filtered data is a bit odd.  The mag value is calculated as mag = (mag*5.0f + MagTotal) / 6.0f where MagTotal is the sensed mag field. This filter is running at 1Hz, but MagTotal is calculated at 100Hz.

### David Grosher, 2024-10-02

@Scott Hunter do you have any next steps beyond this?

### Scott Hunter, 2024-10-02

@David Grosher  - I’ve been chatting with Eric about putting something together to run in an ironbird to try to capture a fault and more information along with the fault. 
I need to check the config file on Edge-DKT-01/407. My memory says I had to change the tolerances to get it through self test. If the config is changed, we’ll need to work on the box to get it in the right configuration/orientation. Then we can start fishing for faults.

### Scott Hunter, 2024-10-02

I just looked at the config files on #407 and a couple of very large event log files that happened to be on the SD card.  
In the confi file, I found config values that I would expect to make a fault impossible, magmargin is 6.0 instead of 0.6 and magdelta is 0.3 instead of 3.0. The magmargin is what's driving the ratio test. So instead of the allowable ratio to be 0.4 - 1.6 it's configured to be -4.0 - 6.0. The magdelta parameter is used as a test of the difference between the measured field and the expected field. We don't currently log a message if there's a failure of the magdelta test.
The bigger find is in the log files where I found 3 instances of the ratio test failing with these ridiculously lenient tests. This might not be too tough to isolate after all.
Question for you @Eric Brewer @David Grosher - is there anything in particular you'd like to see next? 
I propose:
- Nudge the config parameters closer to something reasonable. Just loose enough that I can make it through a boot cycle.
- Capture failures of the magdelta test (should be included in the next release)
- Capture raw data leading up to the faults and get that data off the VTOLAP (should not be included in the next release)

### David Grosher, 2024-10-02

@Scott Hunter @Eric Brewer That seems reasonable to me.

### Scott Hunter, 2024-10-09

@David Grosher @Eric Brewer 
I did more testing trying to capture the erf value being corrupted and that moved the problem to corruption of the mag value. What I noticed is that the corrupted variables are local (aka automatic) and floats. Given that info, I’m now suspicious of a stack problem. If a task is swapped out and another task writes to the first tasks stack it would be consistent with what we see. This also applies to the floating-point registers/context that has to be saved and restored when a task is swapped out.  
I made a hack build that moved all the locals to file scope in function CalcImuMagFieldOk(), imu.cpp. As I write this it’s been running for ~7 hours without a fault. The previous night's run was averaging a fault every ~4 hours.
If this makes the problem go away, I’ll go back to the failing config and add instrumentation to the code that will capture what tasks are swapping in/out when the fault happens and examine the map file to see which tasks have stacks near each other.

### Scott Hunter, 2024-10-10

Root cause appears to be a missing call to portTASK_USES_FLOATING_POINT() in taskOneHz. I need one more round of testing with a targeted change and all the debug code removed.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V689_240930_145516_pack.zip | archive | 4550 | 2024-10-02 | listed only |
