---
lecture: 2.2
sidebar_position: 4
date: 2023-08-30
topics:
  - A
  - B
  - C
---
import Image from '@site/src/components/Image'
import DisplayFlex from '@site/src/components/DisplayFlex'

### Combinational Logic
- a combinational logic cell, logic circuit, or gate is generally a multiple input, single output system that performs a Boolean function
    <Image src="/attachments/IMG-20231210212215.png" alt="Image"/>
- **Question:** how do we design this Combinational Logic Circuit that takes in $n$ inputs and produces a $V_{out}$ that is either $V_{dd}$ or gnd
## Metal-Oxide Semiconductors
- intuitively we start with a switch: transistors
- _transistors_: can be thought as a switch controlled by its gate signal
    - it either blocks or amplifies a signal
### n-type MOS (NMOS)
- n-type source and drain, p-type substrate
- +ve charge allows electrons to move from source to drain
    <Image src="/attachments/IMG-20231210212242.png" alt="Image"/>
- nmos switch closes when switch control input is high
- [nmos pass a _strong 0_ and _weak 1_](https://siliconvlsi.com/why-nmos-pass-strong-0-and-weak-1/)
    - 0 in → exactly 0 out
    - $V_{DD}$ in → $V_{DD}-V_{th}$ out
### p-type MOS (PMOS)
- p-type source and drain, n-type substrate
- -ve charge allows holes to move from source to drain
    <Image src="/attachments/IMG-20231210212314.png" alt="Image"/>
- pmos switch closes when switch control input is low
- [pmos pass a _strong 1_ and _weak 0_](https://siliconvlsi.com/why-pmos-pass-strong-1-and-weak-0/)
    - $V_{DD}$ in → $V_{DD}$ out
    - 0 in → $V_{th}$ out
### Complementary MOS (CMOS)
- Switches are good, but how do we get an output of either $V_{DD}$ or GND without the $V_{th}$ difference? We need cmos
- both pmos and nmos used in complementary manner to create Pull-Up Network (PUN) and Pull-Down Network (PDN)
    - if inputs to PUN are satisfied, pmoses in PUN turn on and brings $V_{DD}$ to output
    - if inputs to PDN are satisfied, nmoses in PDN turn on and brings GND to output
    <DisplayFlex>
    <div style={{ flex: '33%' }}>
    <Image src="/attachments/IMG-20231210212444.png" alt="Image"/>
    </div>
    <div style={{ flex: '33%' }}>
    <Image src="/attachments/IMG-20231210212453.png" alt="Image"/>
    </div>
    <div style={{ flex: '33%' }}>
    <Image src="/attachments/IMG-20231210212501.png" alt="Image"/>
    </div>
    </DisplayFlex>
- importantly, PUN and PDN are never simultaneously on
    - no direct path from $V_{DD}$ to GND → low power dissipation
### CMOS Transmission Gates (Pass Gates)
- cmos Transition Gate (TG) consists of 1 nmos and 1 pmos transistor connected in parallel
- cmos TG operates as a bidirectional switch between A and B, controlled by C
    <Image src="/attachments/IMG-20231210212527.png" alt="Image"/>
- in larger systems
	<DisplayFlex>
    <div style={{ flex: '50%' }}>
    <Image src="/attachments/IMG-20231210212552.png" alt="Image"/>
    </div>
    <div style={{ flex: '50%' }}>
    <Image src="/attachments/IMG-20231210212559.png" alt="Image"/>
    </div>
    </DisplayFlex>
### NOR Gate
<DisplayFlex>
<div style={{ flex: '30%' }}>
| A   | B   | Out |
| --- | --- | --- |
| 0   | 0   | 1   |
| 0   | 1   | 0   |
| 1   | 0   | 0   |
| 1   | 1   | 0   |

</div>
<div style={{ flex: '30%' }}>
<Image src="/attachments/IMG-20231210212630.png" alt="Image"/>
</div>
</DisplayFlex>
- if A and B both 0, $V_{dd}$ → Out
- if A or B is 1, nothing from $V_{dd}$, and A or B or both pulls Out to gnd
- the top part is the PUN, bottom part is PDN
### NAND Gate
<DisplayFlex>
<div style={{ flex: '30%' }}>
| A   | B   | Out |
| --- | --- | --- |
| 0   | 0   | 1   |
| 0   | 1   | 1   |
| 1   | 0   | 1   |
| 1   | 1   | 0   |

</div>
<div style={{ flex: '30%' }}>
<Image src="/attachments/IMG-20231210212710.png" alt="Image"/>
</div>
</DisplayFlex>
- PUN: $F = \overline A + \overline B = \overline {AB}$
- PDN: $G = AB$
- if A or B is 0, $V_{dd}$ → Out
- if A and B both 1, nothing from $V_{dd}$, and both A and B pulls Out to gnd
- top part is PUN, buttom part is PDN
## Sizing: PMOS vs NMOS
- pmos slower than nmos
    - $\mu \approx \frac L {WR}$
        - where:
            - $\mu:$ mobility of charge carriers in the channel of a MOS transistor
            - $L:$ length of transistor
            - $W:$ width of channel
            - $R:$ resistance of transistor
    - $\mu_p \approx \frac 12 \mu_n$
        - because holes in pmos move slower than electrons in nmos, $R_p \gt R_n$
        - thus, pmos usually have wider channels than nmos, $W_p \gt W_n$
- [sizing required to balance fall and rise time delays](https://www.notion.so/Prelab-5968aa845f8e451095e25ed6f92c299a?pvs=21)
### Input Pattern Effect on Delay
- delay dependent on pattern of inputs
- Low → High
    - both inputs go low, delay is $R_p / 2C_L$
    - 1 input goes low, delay is $R_p / C_L$
    - worst case: $R_p / C_L$
- High → Low
    - both inputs go high, delay is $2R_nC_L$
- $R_p = 2R_n \Rightarrow W_p = W_n$
### Simple CMOS Gates
- sizing of complex cells must have same output current of an inverter with certain size
- $(W/L)_{PUN} / (W/L)_{PDN} \geq 2$ to make up for slow pmos
	<Image src="/attachments/IMG-20231210212745.png" alt="Image"/>
### Stage Sizing
- Logical effort can be used to calculate best stage sizing for gates in each stage