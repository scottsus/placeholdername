---
lecture: 13.1
sidebar_position: 26
date: 2023-11-13
topics:
  - pass transistor
  - cmos
---
import Image from '@site/src/components/Image'

## Dynamic Pass Transistor Circuits
- consider the generalized view of a multistage synchronous circuit shown below
	<Image src="/attachments/IMG-20231211155900.png" alt="Image"/> 
- to drive the pass transistors, 2 non-overlapping clock signals are used
	- this is known as *2-phase clocking*
	<Image src="/attachments/IMG-20231211155900-1.png" alt="Image"/>
### Depletion Load Dynamic Shift Register
- Idea: we can make a sequence of FFs to store a few bits of data to form a register
	- the *shift* implies bits are moved from one FF to the next
- consider this next multistage synchronous circuit
	<Image src="/attachments/IMG-20231211155900-2.png" alt="Image"/>
- during the active phase of $\phi_{1}$, $V_{in}$ is transferred into $C_{in1}$ → valid output voltage is the inverse of input $V_{in}$
- when $\phi_2$ becomes active during the next phase, the output voltage level from stage 1 is transferred into the 2nd stage input capacitance $C_{in2}$ → valid output voltage of stage 2 is determined
	- during this time, $C_{in1}$ retains its previous level via charge storage
	- when $\phi_1$ becomes active again, the original data bit written into the register during the previous cycle is transferred into stage 3, and stage 1 can accept the next data bit
- for every active phase, a clock $\frac12$ period must be long enough to allow input cap $C_{in}$ to charge up or down, and the logic level to propagate to the output by charging $C_{out}$
### Dynamic 2-Stage Circuit
- the same operation principle used in the shift register above is used for synchronous depletion nmos logic 1
	<Image src="/attachments/IMG-20231211155901.png" alt="Image"/>
- note: to guarantee correct logic levels are propagated during each active clock cycle, the clock $\frac12$ period length must be longer than the largest single stage propagation delay
## Dynamic CMOS Logic
- significantly reduces number of transistors used to implement any logic function (compared to CMOS) with 0 static power consumption
- Idea:
	1. *precharge* output node capacitance
	2. *evaluating* output level according to applied inputs
- by having the precharging phase, this circuit is faster because we no longer need the PUN ⚡️
- Suppose we have a dynamic cmos logic gate implementing the complex boolean function $F=(A_1A_2A_3+B_1B_2)'$
	<Image src="/attachments/IMG-20231211155901-1.png" alt="Image"/>
- then the graph can be modeled as
	<Image src="/attachments/IMG-20231211155901-2.png" alt="Image"/>
- when clock is low (precharge phase), $M_p$ is conducting while $M_e$ is off
	→ $V_{out}=V_{DD}$
- when clock signal is high (evaluation phase), $M_p$ is off while $M_e$ is on
	→ $V_{out}$ depends on input voltage levels
	1. if $F$ is true, then $V_{out}$ will be pulled to GND
	2. say A1 or B1 is 0, then $V_{out}$ will retain its previous capacitance
### Cascading Dynamic CMOS Logic
- during the precharging phase, $V_{out1}$ and $V_{out2}$ are pulled up, and external inputs are applied
- assume input variables of stage 1 are such that $V_{out1}$ will drop to logic 0 during the eval phase
	<Image src="/attachments/IMG-20231211155901-3.png" alt="Image"/>
- <span style={{ color: '#f55656' }}>Problem:</span> there is an issue when dynamic cmos is cascaded
	1. when eval phase begins, $V_{out1}$ and $V_{out2}$ are initially logic 1 ($V_{out1}$ eventually drops to the correct logic level after a certain time delay)
	2. during this transition, $V_{out1}$ is suggesting $V_{out2}$ to be low at first → $V_{out2}$ at the end of the eval phase may be erroneously low
	3. although $V_{out1}$ eventually settles to correct value, after stored charge is drained, correction of $V_{out2}$ is not possible without PUN
		<Image src="/attachments/IMG-20231211155901-4.png" alt="Image"/>
