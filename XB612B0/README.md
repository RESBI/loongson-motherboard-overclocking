# XB612B0

3B6000 + 7A2000 dev board from Loongson. Everything is based on extracted bios file `Extracted20250501/3B6000.bin` from whom already got the board. Thanks 小胖 ([bilibili page](https://www.bilibili.com/video/BV1gDGez8EfG)) for testing these firmwares, thanks group members for providing hints on AVS setting part. 

# Overclocking settings

## Main clock

The original setting from the firmware was configured the CPU to 2300 MHz, which is pretty conservative. 
```c
unsigned char ucDataBlock[8] = {
	// Offset 0x00000E4C to 0x00000E53
	0x4D, 0x91, 0x41, 0x16, 0xAD, 0xA1, 0x08, 0x03
};
```
```assembly
4D 91 41 16 : lu32i.d    $t1, 0x20c8a
AD A1 08 03 : lu52i.d    $t1, $t1, 0x228
```

the parameter write into `0x1fe001b0` register could be calculated by following the datasheet of 3A6000, I provide some examples here. For further detail, see `MainClockIn0x1fe001b0.py`.

### 2350 MHz

Recommand Vcore: 1150 mV

```assembly
AD 91 41 16 : lu32i.d    $t1, 0x20c8d
AD D1 08 03 : lu52i.d    $t1, $t1, 0x234
```

### 2400 MHz
Recommand Vcore: 1200 mV

```assembly
0D 92 41 16 : lu32i.d    $t1, 0x20c90
AD 01 09 03 : lu52i.d    $t1, $t1, 0x240
```

### 2450 MHz
Recommand Vcore: 1200 mV

```assembly
6D 92 41 16 : lu32i.d    $t1, 0x20c93
AD 31 09 03 : lu52i.d    $t1, $t1, 0x24c
```

### 2500 MHz

Recommand Vcore: 1200 mV

```assembly
CD 92 41 16 : lu32i.d    $t1, 0x20c96
AD 61 09 03 : lu52i.d    $t1, $t1, 0x258
```

### 2600 MHz
Recommand Vcore: 1200 mV

```assembly
8D 93 41 16 : lu32i.d    $t1, 0x20c9c
AD C1 09 03 : lu52i.d    $t1, $t1, 0x270
```

### 2650 MHz
Recommand Vcore: 1250 mV

```assembly
ED 93 41 16 : lu32i.d    $t1, 0x20c9f
AD F1 09 03 : lu52i.d    $t1, $t1, 0x27c
```

### 2700 MHz
Recommand Vcore: 1250 mV

```assembly
4D 94 41 16 : lu32i.d    $t1, 0x20ca2
AD 21 0A 03 : lu52i.d    $t1, $t1, 0x288
```

### 2750 MHz

You really shouldn't try this or any futher!

Recommand Vcore: 1300 mV

```assembly
AD 94 41 16 : lu32i.d    $t1, 0x20ca5
AD 51 0A 03 : lu52i.d    $t1, $t1, 0x294
```
## Voltage

### AVS Voltage setting

in func `@0x1c00220c`, CPU Core voltage and DDR RAM voltage was setted by calling the function `@0x1c001f44` and the 2nd parameter is voltage in mV.

#### CPU Core Voltage
```assembly
ram:1c002238 17 f8 91 02     addi.w     $s0, $zero, 0x47e	;1150
```

### DDR Voltage

this is relatively low, too. Recommand value is 1200~1250 mV for 3200 MT/s sticks.

```assembly
ram:1c002278 05 f8 91 02     addi.w     $a1, $zero, 0x47e	;1150
```
