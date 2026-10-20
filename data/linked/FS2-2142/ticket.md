# FS2-2142: VTOL - Eliminate unterminated while loop in I2C code

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-08-05
- **Updated:** 2024-09-18
- **Resolved:** 2024-09-18
- **Reporter:** Scott Hunter
- **Assignee:** Scott Hunter
- **Creator:** Scott Hunter
- **Parent:** FS2-2281 I2C Initialization
- **Links:** relates to FS2-2143 (XCOMM - Eliminate unterminated while loop in I2C code); relates to FS2-2143 (XCOMM - Eliminate unterminated while loop in I2C code)
- **Epic Link:** FS2-2281
- **Sprint:** FS2 Sprint 24, FS2 Sprint 22, FS2 Sprint 23

## Description

In drv_i2c_static.c, we need to eliminate this unterminated while loop and do something more appropriate.
This needs to be implemented for each of the 3 I2C interfaces.

```
while(I2C2CONbits.PEN) {};  // wait for it
```

## Comments (2)

### Scott Hunter, 2024-08-06

What we’ve learned so far:
- The unterminated while loop in the VTOL code is only used on I2C2 which communicates with the (unused) potentiometer and RTC. The I2C4 initialization code that checks for the I2C4CONbits.PEN bit to go from 1 to zero is commented out and we don’t have any devices on I2C1. The same is true for XCOMM but I’m not sure if we use I2C1 on the XCOMM board. Was this Gordon’s solution to a problem with the interface?
- I measured the time it takes for I2CXCONbits.PEN to clear and found worst case is ~1010 ticks at startup and a nominal 275 when re-initializing based on debug code forcing a reset. I then used a simple integer decrementing to limit that unterminated while loop to ~2000 ticks. That count down value is 300. So, we can initialize our counter, kt=300 and execute while(I2CXCONbits.PEN && kt){kt--;} to put an upper limit of ~2000 clock ticks on the I2C re-initialize step. It’s a bit crude but simple and robust. Definitely a better option than a while loop that doesn’t terminate.
- Since the I2C4CONbits.PEN check is commented out on the mag’s I2C interface it may be that was Gordon’s chosen path to eliminate the infinite loop. There’s no real down-side to not checking the flag if the interface is broken, it’s not going to work anyway. If/when we get a chance to redo this interface the fact that it timed-out could be used to handle a fault condition more gracefully.
- I noticed code in the VTOL and XCOMM where I2C4 is being referenced when it seems like it should be I2C1 (see below).  The usage is consistent for the DRV_I2CX_BaudRateSet() functions. I don’t understand why these indices are used. I don’t understand where the Microchip provided code ends and Edge code begins.


```
void DRV_I2C1_BaudRateSet(I2C_BAUD_RATE baudRate)
{
    /* Disable I2C1 */
    PLIB_I2C_Disable(I2C_ID_4);
    
    /* Change baud rate */
    PLIB_I2C_BaudRateSet(I2C_ID_4, SYS_CLK_PeripheralFrequencyGet(CLK_BUS_PERIPHERAL_2), baudRate);

    /* Low frequency is enabled (**NOTE** PLIB function revereted) */
    PLIB_I2C_HighFrequencyEnable(I2C_ID_4);
 
    /* Enable I2C1 */
    PLIB_I2C_Enable(I2C_ID_4);       
}

```
@David Grosher - In case you’re interested.

### Scott Whitney, 2024-09-11

VTOL merges back to main

## Attachments (0)
