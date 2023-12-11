---
lecture: 2.1
sidebar_position: 3
date: 2023-08-28
topics:
  - Moore's Law
  - Y-Chart
  - scaling
---
import Image from '@site/src/components/Image'
import DisplayFlex from '@site/src/components/DisplayFlex'

## Moore’s Law
- the number of transistors on a circuit doubles every 18-24 months
    - decreasing minimum feature size
- International Technology Roadmap for Semiconductors (ITRS): 15-year assessment of the semiconductor industry’s future technology requirements
    - chip size, number of transistors, DRAM capacity, max clock frequency, min supply voltage, max power dissipation, max number of I/O pins
- important for delays to get less, because energy is a function of BOTH power and **time**
- increasing HW design productivity (using SW)
### Die Cost
- Yield $Y$ = number of good chips per wafer / total number of chips per wafer x 100%
- die cost = wafer cost / (dies per wafer x die yield)
    - die cost = $f$(die area)$^4$
### Multilayer VLSI
- cross section of a 5-layer chip
    <DisplayFlex>
    <div style={{ flex: '50%' }}>
    <Image src="/attachments/IMG-20231210211233.png" alt="Image"/>
    </div>
    <div style={{ flex: '50%' }}>
    <Image src="/attachments/IMG-20231210211833.png" alt="Image"/>
    </div>
    </DisplayFlex>
### System-on-Chip (SoC)
- SoC integrates all the components of a hybrid system on a single substrate rather than building a conventional printed circuit board
- **Advantages**
    - compact system realization
    - cost effective
    - higher speed, performance, reliability
- typical SoC components:
    - microcontroller/microprocessor, memory blocks, oscillators
    - peripherals (counter/timer, reset, USB, Ethernet)
    - ADC/DAC, voltage regulators, power-management systems
		<Image src="/attachments/IMG-20231210211320.png" alt="Image"/>
## Y-Chart
- structural, behavioral, geometrical views
    1. behavioral: algorithm → FSM → module description → boolean expression
    2. structural: processor → register → leaf cell → transistor
    3. geometrical: chip floorplan → module placement → cell placement → mask
### VLSI Design Flow
<Image src="/attachments/IMG-20231210211339.png" alt="Image"/>
### Structured Design Principles
- Hierarchy: top level → low level
- Regularity: all 500 adders must behave the exact same way
- Modularity: well-defined behavior + I/O pins
- Locality: avoid global wires as much as possible
### VLSI Design Styles
<Image src="/attachments/IMG-20231210211354.png" alt="Image"/>
### Challenges in Digital Design
<DisplayFlex>
<div style={{ flex: '33%' }}>
**Miscroscopic Problems**
- ultra high speed design
- interconnect
- noise, crosstalk
- reliability, manufacturability
- power dissipation
</div>
<div style={{ flex: '33%' }}>
**Macroscopic Issues**
- time-to-market
- millions of gates
- high-level abstractions
- reuse & IP
- predictability
</div>
</DisplayFlex>
