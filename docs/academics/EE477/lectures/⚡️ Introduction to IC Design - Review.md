---
lecture: 1.2
sidebar_position: 2
date: 2023-08-23
topics:
  - review
  - transistors
  - logic gates
---
import Image from '@site/src/components/Image'
import TwoColumns from '@site/src/components/TwoColumns'

### Evolution of Transistors in Integrated Circuits
- BJT in Bell Labs → single transistor → CMOS gate → first microprocessor → VLSI → ULSI → System-on-Chip
- first ever computer: Babbage Difference Engine (1832)
	<TwoColumns>
		<div style={{ flex: '33%' }}>
		<Image src="/attachments/IMG-20231210192506.png" alt="Image"/>
		</div>
		<div style={{ flex: '33%' }}>
		**25,000 parts, £17,470**
		</div>
	</TwoColumns>
- first **electronic** computer: ENIAC (1946)
### MOS Transistor Review
- [Amazing video by Veritasium explaining how an NMOS transistor works](https://www.youtube.com/watch?v=IcrBqCFLHIY&ab_channel=Veritasium)
    1. n-type semiconductors are placed at the ends of a transistor, single p-type in the middle
    2. naturally, electrons from n-type move towards p-type to fill the +ve holes
    3. after a while, the n-type | p-type barrier becomes -vely charged, preventing other electrons from moving from n-type to p-type
    4. only a positive charge from the **gate** will allow electrons to travel from n-type to p-type again
### Gates
- transistors in series: AND, transistors in parallel: OR
- AND, OR gate truth tables
- NOT gate
- NAND and NOR gates
    <Image src="/attachments/IMG-20231210191411.png" alt="Image"/>
- XOR and XNOR gates
    <Image src='/attachments/IMG-20231210191424.png' alt='Image'/>
### Functions and Logic Networks
- combinational vs sequential
- logic gates → commonly used functional blocks
    - muxes, adders, ALUs
### Delays
- linear structure
    <Image src="/attachments/IMG-20231210191445.png" alt="Image"/>
- Ripple Carry Adders (RCAs)
### Clock Signals
- alternating high/low voltage pulse train
- _frequency_ (Hz): number of cycles per second
### D Flip-Flop
<Image src="/attachments/IMG-20231210191521.png" alt="Image"/>
### Registers
<Image src="/attachments/IMG-20231210191533.png" alt="Image"/>
### Pipelining
<TwoColumns>
<div>
<Image src="/attachments/IMG-20231210192009.png" alt="Image"/>
</div>
<div>
<Image src="/attachments/IMG-20231210191940.png" alt="Image"/>
</div>
</TwoColumns>
### Power
- Instantaneous power
	$\\ p(t) = v(t)i(t) = V_{supply}i(t)$
- Peak power
	$\\ P_{peak} = V_{supply} i_{peak}$
- Average power
	$\\ P_{ave} = \frac 1T \int_t^{t+T} p(t) dt$
	$\\ = \frac {V_{supply}}T \int_t^{t+T} i_{supply}(t) dt$
### First Order Resistor-Capacitor (RC) Network
- energy consumed transitioning digital logic 0 to 1

	$
	\begin{aligned}
    &\quad E_{0 \rightarrow 1} = \int_0^T p(t) dt &\\
    &\quad =V_{dd} \int_0^T i_{supply}(t) dt &\\
    &\quad =V_{dd} \int_0^{V_{dd}} C_L dV_{out} &\\
    &\quad = C_L (V_{dd})^2 &\\
    \end{aligned}
	$
- energy stored in load capacitance during charge & discharge

	$
	\begin{aligned}
    &\quad E_{cap} = \int_0^T p_{cap}(t) dt &\\
    &\quad = \int_0^T V_{out} i_{cap}(t) dt &\\
    &\quad = \int_0^{V_{dd}} C_L V_{out} dV_{out} &\\
    &\quad = \frac 12 C_L (V_{dd})^2 &\\
    \end{aligned}
	$
- $\frac 12 C_L(V_{dd})^2$ is lost during the charge & discharge process to resistor $R$
### Reliability: Noise in Digital Integrated Circuits
<Image src="/attachments/IMG-20231210192047.png" alt="Image"/>