---
lecture: 3.2
sidebar_position: 6
date: 2023-09-06
topics:
  - inverter
  - Euler's Path
  - layouts
---
import Image from '@site/src/components/Image'
import DisplayFlex from '@site/src/components/DisplayFlex'

- nmos: n-type source and drain, p-type substrate    
- pmos: p-type source and drain, n-type substrate
- cmos example
	<Image src="/attachments/IMG-20231210220528.png" alt="Image"/>
### Inverter Layout
- **2 Possible Configurations**
	<DisplayFlex>
	<div style={{ flex: '40%' }}>
	<Image src="/attachments/IMG-20231210220832.png" alt="Image"/>
	</div>
	<div style={{ flex: '40%' }}>
	<Image src="/attachments/IMG-20231210220848.png" alt="Image"/>
	</div>
	</DisplayFlex>
- **Layout View**
   <Image src="/attachments/IMG-20231210220911.png" alt="Image"/>
### NAND Schematic and Layout
<DisplayFlex>
<div style={{ flex: '20%' }}>
<Image src="/attachments/IMG-20231210221258.png" alt="Image"/>
</div>
<div style={{ flex: '40%' }}>
<Image src="/attachments/IMG-20231210221324.png" alt="Image"/>
</div>
<div style={{ flex: '33%' }}>
<Image src="/attachments/IMG-20231210221356.png" alt="Image"/>
</div>
</DisplayFlex>
### NOR Schematic and Layout
<Image src="/attachments/IMG-20231210221424.png" alt="Image"/>
## Complex Gates
- consider the following boolean function: $Z = \overline {A(D+E)+BC}$
	<Image src="/attachments/IMG-20231210221446.png" alt="Image"/>
- all parallel connections in nmos PDN will correspond to a series connection in pmos PUN
### Complex CMOS Logic Gates
- a series connection in PDN correspond to parallel connections in PUN
    1. each driver transistor in PDN is represented by an edge
        - each internal node is represented by a vertex in PDN
    2. a new vertex is created within each confined area in PDN
        - neighboring vertices are connected by edges which cross each edge in PDN only once
        - this graph represents PUN
    <Image src="/attachments/IMG-20231210221510.png" alt="Image"/>
- the number of diffusion breaks can be minimized by changing ordering of polysilicon columns
- simple method for finding optimum gate ordering is the **Euler-path** approach
    - find a common Euler path for both PDN and PUN graphs
    - polysilicon columns can be arranged according to the sequence in Euler path
- an easier method is just **trial and error** until we find a path that satisfied both PUN and PDN
- diffusion will be unbroken if identically labeled Euler paths can be found for p and n trees
- Optimize stick-diagram layout of complex CMOS logic gate
	<Image src="/attachments/IMG-20231210221548.png" alt="Image"/>
## CMOS Full Adder Circuit
<Image src="/attachments/IMG-20231210221605.png" alt="Image"/>
### Sum and $c_{out}$ circuit for a 1-bit FA
<Image src="/attachments/IMG-20231210221620.png" alt="Image"/>
### FA Layout
<Image src="/attachments/IMG-20231210221635.png" alt="Image"/>
### Performance-Optimized, Compact Mask Layout
<Image src="/attachments/IMG-20231210221654.png" alt="Image"/>
### FA Waveform Extraction
<Image src="/attachments/IMG-20231210221708.png" alt="Image"/>
### Ripple Carry Adder (RCA)
- simplest FA circuit can be constructed by a cascade of FA’s
    - each adder performs a 2-bit addition → produces corresponding sum bit → passes $c_{out}$
- speed of RCA limited by delay of carry bits ripplying through carry chain
- path from $c_0$ to $s_7$ is the **critical path**