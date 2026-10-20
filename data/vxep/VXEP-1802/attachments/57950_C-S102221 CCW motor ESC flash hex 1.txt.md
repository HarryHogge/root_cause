# C-S102221 CCW motor ESC flash hex 1.txt

Attachment 57950, text, 38 KB, added 2026-05-22 by John Clark.

C:\Users\dmiyahara>avrdude.exe -C C:\Users\dmiyahara\Downloads\kkmulticopterflashtool_0.77\lib\avrdude\windows\usbtiny\avrdude.conf -p m8 -P usb -c usbtiny -vvvvv -U flash:r:flash.hex:i

avrdude.exe: Version 5.4-arduino, compiled on Oct 11 2007 at 19:12:32
             Copyright (c) 2000-2005 Brian Dean, http://www.bdmicro.com/

             System wide configuration file is "C:\Users\dmiyahara\Downloads\kkmulticopterflashtool_0.77\lib\avrdude\windows\usbtiny\avrdude.conf"

             Using Port            : usb
             Using Programmer      : usbtiny
             AVR Part              : ATMEGA8
             Chip Erase delay      : 10000 us
             PAGEL                 : PD7
             BS2                   : PC2
             RESET disposition     : dedicated
             RETRY pulse           : SCK
             serial program mode   : yes
             parallel program mode : yes
             Timeout               : 200
             StabDelay             : 100
             CmdexeDelay           : 25
             SyncLoops             : 32
             ByteDelay             : 0
             PollIndex             : 3
             PollValue             : 0x53
             Memory Detail         :

                                      Block Poll               Page                       Polled
               Memory Type Mode Delay Size  Indx Paged  Size   Size #Pages MinW  MaxW   ReadBack
               ----------- ---- ----- ----- ---- ------ ------ ---- ------ ----- ----- ---------
               eeprom         4    20   128    0 no        512    0      0  9000  9000 0xff 0xff
                 Memory Ops:
                   Oeration     Inst Bit  Bit Type  Bitno  Value
                   -----------  --------  --------  -----  -----
                   READ               31     VALUE      7      1
                                      30     VALUE      6      0
                                      29     VALUE      5      1
                                      28     VALUE      4      0
                                      27     VALUE      3      0
                                      26     VALUE      2      0
                                      25     VALUE      1      0
                                      24     VALUE      0      0
                                      23     VALUE      7      0
                                      22     VALUE      6      0
                                      21    IGNORE      5      0
                                      20    IGNORE      4      0
                                      19    IGNORE      3      0
                                      18    IGNORE      2      0
                                      17    IGNORE      1      0
                                      16   ADDRESS      8      0
                                      15   ADDRESS      7      0
                                      14   ADDRESS      6      0
                                      13   ADDRESS      5      0
                                      12   ADDRESS      4      0
                                      11   ADDRESS      3      0
                                      10   ADDRESS      2      0
                                       9   ADDRESS      1      0
                                       8   ADDRESS      0      0
                                       7    OUTPUT      7      0
                                       6    OUTPUT      6      0
                                       5    OUTPUT      5      0
                                       4    OUTPUT      4      0
                                       3    OUTPUT      3      0
                                       2    OUTPUT      2      0
                                       1    OUTPUT      1      0
                                       0    OUTPUT      0      0
                   WRITE              31     VALUE      7      1
                                      30     VALUE      6      1
                                      29     VALUE      5      0
                                      28     VALUE      4      0
                                      27     VALUE      3      0
                                      26     VALUE      2      0
                                      25     VALUE      1      0
                                      24     VALUE      0      0
                                      23     VALUE      7      0
                                      22     VALUE      6      0
                                      21    IGNORE      5      0
                                      20    IGNORE      4      0
                                      19    IGNORE      3      0
                                      18    IGNORE      2      0
                                      17    IGNORE      1      0
                                      16   ADDRESS      8      0
                                      15   ADDRESS      7      0
                                      14   ADDRESS      6      0
                                      13   ADDRESS      5      0
                                      12   ADDRESS      4      0
                                      11   ADDRESS      3      0
                                      10   ADDRESS      2      0
                                       9   ADDRESS      1      0
                                       8   ADDRESS      0      0
                                       7     INPUT      7      0
                                       6     INPUT      6      0
                                       5     INPUT      5      0
                                       4     INPUT      4      0
                                       3     INPUT      3      0
                                       2     INPUT      2      0
                                       1     INPUT      1      0
                                       0     INPUT      0      0
                                      Block Poll               Page                       Polled
               Memory Type Mode Delay Size  Indx Paged  Size   Size #Pages MinW  MaxW   ReadBack
               ----------- ---- ----- ----- ---- ------ ------ ---- ------ ----- ----- ---------
               flash         33    10    64    0 yes      8192   64    128  4500  4500 0xff 0x00
                 Memory Ops:
                   Oeration     Inst Bit  Bit Type  Bitno  Value
                   -----------  --------  --------  -----  -----
                   READ_LO            31     VALUE      7      0
                                      30     VALUE      6      0
                                      29     VALUE      5      1
                                      28     VALUE      4      0
                                      27     VALUE      3      0
                                      26     VALUE      2      0
                                      25     VALUE      1      0
                                      24     VALUE      0      0
                                      23     VALUE      7      0
                                      22     VALUE      6      0
                                      21     VALUE      5      0
                                      20     VALUE      4      0
                                      19   ADDRESS     11      0
                                      18   ADDRESS     10      0
                                      17   ADDRESS      9      0
                                      16   ADDRESS      8      0
                                      15   ADDRESS      7      0
                                      14   ADDRESS      6      0
                                      13   ADDRESS      5      0
                                      12   ADDRESS      4      0
                                      11   ADDRESS      3      0
                                      10   ADDRESS      2      0
                                       9   ADDRESS      1      0
                                       8   ADDRESS      0      0
                                       7    OUTPUT      7      0
                                       6    OUTPUT      6      0
                                       5    OUTPUT      5      0
                                       4    OUTPUT      4      0
                                       3    OUTPUT      3      0
                                       2    OUTPUT      2      0
                                       1    OUTPUT      1      0
                                       0    OUTPUT      0      0
                   READ_HI            31     VALUE      7      0
                                      30     VALUE      6      0
                                      29     VALUE      5      1
                                      28     VALUE      4      0
                                      27     VALUE      3      1
                                      26     VALUE      2      0
                                      25     VALUE      1      0
                                      24     VALUE      0      0
                                      23     VALUE      7      0
                                      22     VALUE      6      0
                                      21     VALUE      5      0
                                      20     VALUE      4      0
                                      19   ADDRESS     11      0
                                      18   ADDRESS     10      0
                                      17   ADDRESS      9      0
                                      16   ADDRESS      8      0
                                      15   ADDRESS      7      0
                                      14   ADDRESS      6      0
                                      13   ADDRESS      5      0
                                      12   ADDRESS      4      0
                                      11   ADDRESS      3      0
                                      10   ADDRESS      2      0
                                       9   ADDRESS      1      0
                                       8   ADDRESS      0      0
                                       7    OUTPUT      7      0
                                       6    OUTPUT      6      0
                                       5    OUTPUT      5      0
                                       4    OUTPUT      4      0
                                       3    OUTPUT      3      0
                                       2    OUTPUT      2      0
                                       1    OUTPUT      1      0
                                       0    OUTPUT      0      0
                   LOADPAGE_LO        31     VALUE      7      0
                                      30     VALUE      6      1
                                      29     VALUE      5      0
                                      28     VALUE      4      0
                                      27     VALUE      3      0
                                      26     VALUE      2      0
                                      25     VALUE      1      0
                                      24     VALUE      0      0
                                      23     VALUE      7      0
                                      22     VALUE      6      0
                                      21     VALUE      5      0
                                      20     VALUE      4      0
                                      19    IGNORE      3      0
                                      18    IGNORE      2      0
                                      17    IGNORE      1      0
                                      16    IGNORE      0      0
                                      15    IGNORE      7      0
                                      14    IGNORE      6      0
                                      13    IGNORE      5      0
                                      12   ADDRESS      4      0
                                      11   ADDRESS      3      0
                                      10   ADDRESS      2      0
                                       9   ADDRESS      1      0
                                       8   ADDRESS      0      0
                                       7     INPUT      7      0
                                       6     INPUT      6      0
                                       5     INPUT      5      0
                                       4     INPUT      4      0
                                       3     INPUT      3      0
                                       2     INPUT      2      0
                                       1     INPUT      1      0
                                       0     INPUT      0      0
                   LOADPAGE_HI        31     VALUE      7      0
                                      30     VALUE      6      1
                                      29     VALUE      5      0
                                      28     VALUE      4      0
                                      27     VALUE      3      1
                                      26     VALUE      2      0
                                      25     VALUE      1      0
                                      24     VALUE      0      0
                                      23     VALUE      7      0
                                      22     VALUE      6      0
                                      21     VALUE      5      0
                                      20     VALUE      4      0
                                      19    IGNORE      3      0
                                      18    IGNORE      2      0
                                      17    IGNORE      1      0
                                      16    IGNORE      0      0
                                      15    IGNORE      7      0
                                      14    IGNORE      6      0
                                      13    IGNORE      5      0
                                      12   ADDRESS      4      0
                                      11   ADDRESS      3      0
                                      10   ADDRESS      2      0
                                       9   ADDRESS      1      0
                                       8   ADDRESS      0      0
                                       7     INPUT      7      0
                                       6     INPUT      6      0
                                       5     INPUT      5      0
                                       4     INPUT      4      0
                                       3     INPUT      3      0
                                       2     INPUT      2      0
                                       1     INPUT      1      0
                                       0     INPUT      0      0
                   WRITEPAGE          31     VALUE      7      0
                                      30     VALUE      6      1
                                      29     VALUE      5      0
                                      28     VALUE      4      0
                                      27     VALUE      3      1
                                      26     VALUE      2      1
                                      25     VALUE      1      0
                                      24     VALUE      0      0
                                      23     VALUE      7      0
                                      22     VALUE      6      0
                                      21     VALUE      5      0
                                      20     VALUE      4      0
                                      19   ADDRESS     11      0
                                      18   ADDRESS     10      0
                                      17   ADDRESS      9      0
                                      16   ADDRESS      8      0
                                      15   ADDRESS      7      0
                                      14   ADDRESS      6      0
                                      13   ADDRESS      5      0
                                      12    IGNORE      4      0
                                      11    IGNORE      3      0
                                      10    IGNORE      2      0
                                       9    IGNORE      1      0
                                       8    IGNORE      0      0
                                       7    IGNORE      7      0
                                       6    IGNORE      6      0
                                       5    IGNORE      5      0
                                       4    IGNORE      4      0
                                       3    IGNORE      3      0
                                       2    IGNORE      2      0
                                       1    IGNORE      1      0
                                       0    IGNORE      0      0
                                      Block Poll               Page                       Polled
               Memory Type Mode Delay Size  Indx Paged  Size   Size #Pages MinW  MaxW   ReadBack
               ----------- ---- ----- ----- ---- ------ ------ ---- ------ ----- ----- ---------
               lfuse          0     0     0    0 no          1    0      0  2000  2000 0x00 0x00
                 Memory Ops:
                   Oeration     Inst Bit  Bit Type  Bitno  Value
                   -----------  --------  --------  -----  -----
                   READ               31     VALUE      7      0
                                      30     VALUE      6      1
                                      29     VALUE      5      0
                                      28     VALUE      4      1
                                      27     VALUE      3      0
                                      26     VALUE      2      0
                                      25     VALUE      1      0
                                      24     VALUE      0      0
                                      23     VALUE      7      0
                                      22     VALUE      6      0
                                      21     VALUE      5      0
                                      20     VALUE      4      0
                                      19     VALUE      3      0
                                      18     VALUE      2      0
                                      17     VALUE      1      0
                                      16     VALUE      0      0
                                      15    IGNORE      7      0
                                      14    IGNORE      6      0
                                      13    IGNORE      5      0
                                      12    IGNORE      4      0
                                      11    IGNORE      3      0
                                      10    IGNORE      2      0
                                       9    IGNORE      1      0
                                       8    IGNORE      0      0
                                       7    OUTPUT      7      0
                                       6    OUTPUT      6      0
                                       5    OUTPUT      5      0
                                       4    OUTPUT      4      0
                                       3    OUTPUT      3      0
                                       2    OUTPUT      2      0
                                       1    OUTPUT      1      0
                                       0    OUTPUT      0      0
                   WRITE              31     VALUE      7      1
                                      30     VALUE      6      0
                                      29     VALUE      5      1
                                      28     VALUE      4      0
                                      27     VALUE      3      1
                                      26     VALUE      2      1
                                      25     VALUE      1      0
                                      24     VALUE      0      0
                                      23     VALUE      7      1
                                      22     VALUE      6      0
                                      21     VALUE      5      1
                                      20     VALUE      4      0
                                      19     VALUE      3      0
                                      18     VALUE      2      0
                                      17     VALUE      1      0
                                      16     VALUE      0      0
                                      15    IGNORE      7      0
                                      14    IGNORE      6      0
                                      13    IGNORE      5      0
                                      12    IGNORE      4      0
                                      11    IGNORE      3      0
                                      10    IGNORE      2      0
                                       9    IGNORE      1      0
                                       8    IGNORE      0      0
                                       7     INPUT      7      0
                                       6     INPUT      6      0
                                       5     INPUT      5      0
                                       4     INPUT      4      0
                                       3     INPUT      3      0
                                       2     INPUT      2      0
                                       1     INPUT      1      0
                                       0     INPUT      0      0
                                      Block Poll               Page                       Polled
               Memory Type Mode Delay Size  Indx Paged  Size   Size #Pages MinW  MaxW   ReadBack
               ----------- ---- ----- ----- ---- ------ ------ ---- ------ ----- ----- ---------
               hfuse          0     0     0    0 no          1    0      0  2000  2000 0x00 0x00
                 Memory Ops:
                   Oeration     Inst Bit  Bit Type  Bitno  Value
                   -----------  --------  --------  -----  -----
                   READ               31     VALUE      7      0
                                      30     VALUE      6      1
                                      29     VALUE      5      0
                                      28     VALUE      4      1
                                      27     VALUE      3      1
                                      26     VALUE      2      0
                                      25     VALUE      1      0
                                      24     VALUE      0      0
                                      23     VALUE      7      0
                                      22     VALUE      6      0
                                      21     VALUE      5      0
                                      20     VALUE      4      0
                                      19     VALUE      3      1
                                      18     VALUE      2      0
                                      17     VALUE      1      0
                                      16     VALUE      0      0
                                      15    IGNORE      7      0
                                      14    IGNORE      6      0
                                      13    IGNORE      5      0
                                      12    IGNORE      4      0
                                      11    IGNORE      3      0
                                      10    IGNORE      2      0
                                       9    IGNORE      1      0
                                       8    IGNORE      0      0
                                       7    OUTPUT      7      0
                                       6    OUTPUT      6      0
                                       5    OUTPUT      5      0
                                       4    OUTPUT      4      0
                                       3    OUTPUT      3      0
                                       2    OUTPUT      2      0
                                       1    OUTPUT      1      0
                                       0    OUTPUT      0      0
                   WRITE              31     VALUE      7      1
                                      30     VALUE      6      0
                                      29     VALUE      5      1
                                      28     VALUE      4      0
                                      27     VALUE      3      1
                                      26     VALUE      2      1
                                      25     VALUE      1      0
                                      24     VALUE      0      0
                                      23     VALUE      7      1
                                      22     VALUE      6      0
                                      21     VALUE      5      1
                                      20     VALUE      4      0
                                      19     VALUE      3      1
                                      18     VALUE      2      0
                                      17     VALUE      1      0
                                      16     VALUE      0      0
                                      15    IGNORE      7      0
                                      14    IGNORE      6      0
                                      13    IGNORE      5      0
                                      12    IGNORE      4      0
                                      11    IGNORE      3      0
                                      10    IGNORE      2      0
                                       9    IGNORE      1      0
                                       8    IGNORE      0      0
                                       7     INPUT      7      0
                                       6     INPUT      6      0
                                       5     INPUT      5      0
                                       4     INPUT      4      0
                                       3     INPUT      3      0
                                       2     INPUT      2      0
                                       1     INPUT      1      0
                                       0     INPUT      0      0
                                      Block Poll               Page                       Polled
               Memory Type Mode Delay Size  Indx Paged  Size   Size #Pages MinW  MaxW   ReadBack
               ----------- ---- ----- ----- ---- ------ ------ ---- ------ ----- ----- ---------
               lock           0     0     0    0 no          1    0      0  2000  2000 0x00 0x00
                 Memory Ops:
                   Oeration     Inst Bit  Bit Type  Bitno  Value
                   -----------  --------  --------  -----  -----
                   READ               31     VALUE      7      0
                                      30     VALUE      6      1
                                      29     VALUE      5      0
                                      28     VALUE      4      1
                                      27     VALUE      3      1
                                      26     VALUE      2      0
                                      25     VALUE      1      0
                                      24     VALUE      0      0
                                      23     VALUE      7      0
                                      22     VALUE      6      0
                                      21     VALUE      5      0
                                      20     VALUE      4      0
                                      19     VALUE      3      0
                                      18     VALUE      2      0
                                      17     VALUE      1      0
                                      16     VALUE      0      0
                                      15    IGNORE      7      0
                                      14    IGNORE      6      0
                                      13    IGNORE      5      0
                                      12    IGNORE      4      0
                                      11    IGNORE      3      0
                                      10    IGNORE      2      0
                                       9    IGNORE      1      0
                                       8    IGNORE      0      0
                                       7    IGNORE      7      0
                                       6    IGNORE      6      0
                                       5    OUTPUT      5      0
                                       4    OUTPUT      4      0
                                       3    OUTPUT      3      0
                                       2    OUTPUT      2      0
                                       1    OUTPUT      1      0
                                       0    OUTPUT      0      0
                   WRITE              31     VALUE      7      1
                                      30     VALUE      6      0
                                      29     VALUE      5      1
                                      28     VALUE      4      0
                                      27     VALUE      3      1
                                      26     VALUE      2      1
                                      25     VALUE      1      0
                                      24     VALUE      0      0
                                      23     VALUE      7      1
                                      22     VALUE      6      1
                                      21     VALUE      5      1
                                      20    IGNORE      4      0
                                      19    IGNORE      3      0
                                      18    IGNORE      2      0
                                      17    IGNORE      1      0
                                      16    IGNORE      0      0
                                      15    IGNORE      7      0
                                      14    IGNORE      6      0
                                      13    IGNORE      5      0
                                      12    IGNORE      4      0
                                      11    IGNORE      3      0
                                      10    IGNORE      2      0
                                       9    IGNORE      1      0
                                       8    IGNORE      0      0
                                       7     VALUE      7      1
                                       6     VALUE      6      1
                                       5     INPUT      5      0
                                       4     INPUT      4      0
                                       3     INPUT      3      0
                                       2     INPUT      2      0
                                       1     INPUT      1      0
                                       0     INPUT      0      0
                                      Block Poll               Page                       Polled
               Memory Type Mode Delay Size  Indx Paged  Size   Size #Pages MinW  MaxW   ReadBack
               ----------- ---- ----- ----- ---- ------ ------ ---- ------ ----- ----- ---------
               calibration    0     0     0    0 no          4    0      0     0     0 0x00 0x00
                 Memory Ops:
                   Oeration     Inst Bit  Bit Type  Bitno  Value
                   -----------  --------  --------  -----  -----
                   READ               31     VALUE      7      0
                                      30     VALUE      6      0
                                      29     VALUE      5      1
                                      28     VALUE      4      1
                                      27     VALUE      3      1
                                      26     VALUE      2      0
                                      25     VALUE      1      0
                                      24     VALUE      0      0
                                      23     VALUE      7      0
                                      22     VALUE      6      0
                                      21    IGNORE      5      0
                                      20    IGNORE      4      0
                                      19    IGNORE      3      0
                                      18    IGNORE      2      0
                                      17    IGNORE      1      0
                                      16    IGNORE      0      0
                                      15     VALUE      7      0
                                      14     VALUE      6      0
                                      13     VALUE      5      0
                                      12     VALUE      4      0
                                      11     VALUE      3      0
                                      10     VALUE      2      0
                                       9   ADDRESS      1      0
                                       8   ADDRESS      0      0
                                       7    OUTPUT      7      0
                                       6    OUTPUT      6      0
                                       5    OUTPUT      5      0
                                       4    OUTPUT      4      0
                                       3    OUTPUT      3      0
                                       2    OUTPUT      2      0
                                       1    OUTPUT      1      0
                                       0    OUTPUT      0      0
                                      Block Poll               Page                       Polled
               Memory Type Mode Delay Size  Indx Paged  Size   Size #Pages MinW  MaxW   ReadBack
               ----------- ---- ----- ----- ---- ------ ------ ---- ------ ----- ----- ---------
               signature      0     0     0    0 no          3    0      0     0     0 0x00 0x00
                 Memory Ops:
                   Oeration     Inst Bit  Bit Type  Bitno  Value
                   -----------  --------  --------  -----  -----
                   READ               31     VALUE      7      0
                                      30     VALUE      6      0
                                      29     VALUE      5      1
                                      28     VALUE      4      1
                                      27     VALUE      3      0
                                      26     VALUE      2      0
                                      25     VALUE      1      0
                                      24     VALUE      0      0
                                      23    IGNORE      7      0
                                      22    IGNORE      6      0
                                      21    IGNORE      5      0
                                      20    IGNORE      4      0
                                      19    IGNORE      3      0
                                      18    IGNORE      2      0
                                      17    IGNORE      1      0
                                      16    IGNORE      0      0
                                      15    IGNORE      7      0
                                      14    IGNORE      6      0
                                      13    IGNORE      5      0
                                      12    IGNORE      4      0
                                      11    IGNORE      3      0
                                      10    IGNORE      2      0
                                       9   ADDRESS      1      0
                                       8   ADDRESS      0      0
                                       7    OUTPUT      7      0
                                       6    OUTPUT      6      0
                                       5    OUTPUT      5      0
                                       4    OUTPUT      4      0
                                       3    OUTPUT      3      0
                                       2    OUTPUT      2      0
                                       1    OUTPUT      1      0
                                       0    OUTPUT      0      0

             Programmer Type : USBTINY
             Description     : USBtiny simple USB programmer

avrdude.exe: Using SCK period of 10 usec
CMD: [ac 53 00 00] [00 00 53 00]
avrdude.exe: AVR device initialized and ready to accept instructions

Reading |                                                    | 0% 0.00sCMD: [30 00 00 00] [00 30 00 1e]
CMD: [30 00 01 00] [00 30 00 93]
Reading | #################                                  | 33% 0.01sCMD: [30 00 02 00] [00 30 00 07]
Reading | ################################################## | 100% 0.01s

avrdude.exe: Device signature = 0x1e9307
CMD: [50 00 00 00] [00 50 00 3f]
avrdude.exe: safemode read 1, lfuse value: 3f
CMD: [50 00 00 00] [00 50 00 3f]
avrdude.exe: safemode read 2, lfuse value: 3f
CMD: [50 00 00 00] [00 50 00 3f]
avrdude.exe: safemode read 3, lfuse value: 3f
avrdude.exe: safemode: lfuse reads as 3F
CMD: [58 08 00 00] [00 58 08 ca]
avrdude.exe: safemode read 1, hfuse value: ca
CMD: [58 08 00 00] [00 58 08 ca]
avrdude.exe: safemode read 2, hfuse value: ca
CMD: [58 08 00 00] [00 58 08 ca]
avrdude.exe: safemode read 3, hfuse value: ca
avrdude.exe: safemode: hfuse reads as CA
avrdude.exe: reading flash memory:

Reading | ################################################## | 100% 8.15s



avrdude.exe: writing output file "flash.hex"

CMD: [50 00 00 00] [00 50 00 3f]
avrdude.exe: safemode read 1, lfuse value: 3f
CMD: [50 00 00 00] [00 50 00 3f]
avrdude.exe: safemode read 2, lfuse value: 3f
CMD: [50 00 00 00] [00 50 00 3f]
avrdude.exe: safemode read 3, lfuse value: 3f
avrdude.exe: safemode: lfuse reads as 3F
CMD: [58 08 00 00] [00 58 08 ca]
avrdude.exe: safemode read 1, hfuse value: ca
CMD: [58 08 00 00] [00 58 08 ca]
avrdude.exe: safemode read 2, hfuse value: ca
CMD: [58 08 00 00] [00 58 08 ca]
avrdude.exe: safemode read 3, hfuse value: ca
avrdude.exe: safemode: hfuse reads as CA
avrdude.exe: safemode: Fuses OK

avrdude.exe done.  Thank you.
