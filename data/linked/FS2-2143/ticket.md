# FS2-2143: XCOMM - Eliminate unterminated while loop in I2C code

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
- **Links:** relates to FS2-2142 (VTOL - Eliminate unterminated while loop in I2C code ); relates to FS2-2142 (VTOL - Eliminate unterminated while loop in I2C code )
- **Epic Link:** FS2-2281
- **Sprint:** FS2 Sprint 24, FS2 Sprint 22, FS2 Sprint 23

## Description

In drv_i2c_static.c, we need to eliminate this unterminated while loop and do something more appropriate.
The change needs to be implemented for each of the 3 I2C interfaces. This same issue exists in the VTOL
 
```
while(I2C2CONbits.PEN) {};  // wait for it
```

## Comments (1)

### Scott Hunter, 2024-09-05

Per https://jenaero.atlassian.net/browse/FS2-2142 a good delay for this loop is 300 counts.  In order to get some visibility into how this is working I’ll add a record of if or how often this loop times-out.
If the nTimeOuts changes from one dump of the ISR table to the next I’ll dump the count.
So, the new code becomes something like:
static int nI2C2TimeOuts=0;
int getI2C2TimeOuts()
{
   return nI2C2TimeOuts;
}
…
toutKt=300;
while(I2C2CONbits.PEN && toutKt--) {};  // wait for it
if ( toutKt == 0 )
{
   nI2C2TimeOuts++;
}

## Attachments (0)
