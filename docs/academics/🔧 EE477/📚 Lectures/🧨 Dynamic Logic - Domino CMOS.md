---
lecture: 13.2
sidebar_position: 27
date: 2023-11-15
topics:
  - domino
---
import Image from '@site/src/components/Image'
import DisplayFlex from '@site/src/components/DisplayFlex'

## Domino CMOS Logic
- a dynamic cmos logic stage must be cascaded with a static cmos inverter stage
	1. during the precharge stage, $V_{out1}$ is precharged to logic 1 → force $V_{out2}$ to go to 0
	2. during the eval phase, $V_{out1}$ either discharged or remains high → $V_{out2}$ charges to high (0 → 1 transition) or remains low
	3. importantly, a 0 and 0 → 1 for $V_{out2}$ will not result in error for next stage - we are effectively disallowing 1 → 0 transitions
- recall this was our diagram for cascading cmos
	<Image src="/attachments/IMG-20231211155902.png" alt="Image"/>
- essentially, domino structure solves the cascading problem by <span style={{ color: '#73e265' }}>removing the 1 → 0 transition</span> of the next nmos input
	- the easiest way to do this is to add a simple inverter after each stage
	<Image src="/attachments/IMG-20231211155956.png" alt="Image"/>
- moreover, domino cmos gates allow significant reduction in number of transistors required to realize any complex boolean function
	<Image src="/attachments/IMG-20231211155956-1.png" alt="Image"/>
### Utilizing Static CMOS with Domino
- conventional static cmos gates can be used together with domino cmos gates in cascaded configuration
- <span style={{ color: '#f56332' }}>Limitation:</span> the number of inverting static logic stages in cascade must be even, so that inputs of the next domino experience only 0 → 1 transitions during eval
### Dual-Rail Domino
- even inversion implies that domino only performs *non-inverting functions*
	- AND, OR ✅
	- NAND, NOR, XOR ❌
- Idea: *dual-rail domino*
	- takes true & complementary inputs
	- produces true & complementary outputs
	<Image src="/attachments/IMG-20231211155957.png" alt="Image"/>
- disadvantage: to build NOR, we also need to build a NAND (inefficient in domino)
### Charge Sharing
- consider the following circuit
	<Image src="/attachments/IMG-20231211155903.png" alt="Image"/>
	- $C_2$ is comparable in size to $C_1$
	- all inputs are initially low, $C_2=0V$
	- during precharge, $C_1$ charged up to $V_{DD}$
	- during eval, if input signal to nmos (in the box) switches from 0 → 1, then the charge from $C_1$ will now be shared with $C_2$, leading to a *charge-sharing phenomenon*
	- the output node voltage after sharing is given by
		$\\ \quad \frac{V_{DD}}{1+C_{2}/C_{1}}$
- <span style={{ color: '#f55656' }}>Problem:</span> if $C_1=C_2$, this may lead to erroneous $V_{out}$
### Preventing the Charge Sharing Problem
- Idea 1: add a weak pmos pullup device with small $W/L$ to dynamic cmos stage output, essentially forcing a high $V_x$ unless there is a strong pulldown path between $V_x$ and ground
	<Image src="/attachments/IMG-20231211155957-1.png" alt="Image"/>
	1. as $V_x$ degrades → $V_{DS}\neq0$ → pmos turns on
	2. $V_x$ pulled back up to $V_{DD}$
- Idea 2: separate pmos transistors to precharge all intermediate nodes in nmos pulldown tree
	<Image src="/attachments/IMG-20231211155957-2.png" alt="Image"/>
	- multiple percharge transistors also enables us to use precharged intermediate nodes as resources for additional outputs (multiple-output domino)
### Multiple-Output Domino
- consider the following realization of 4 boolean functions of 9 variables using a single domino cmos logic gate
	<Image src="/attachments/IMG-20231211155957-3.png" alt="Image"/>
- comparing this with
	1. 4 separate standard cmos logic gates
	2. 4 separate single-output domino cmos circuits
- this is much more compact!
### Transistor Sizing
- adjusting nmos transistor sizes in pulldown path can reduce discharge time
- recall that the best performance is obtained with a *graded sizing* of nmos transistors in series
	- similarly, bottom-most transistor should be sized the largest
	<Image src="/attachments/IMG-20231211155958.png" alt="Image"/>
- let
	$\\ \quad C_L$ be the load capacitance
	$\\ \quad C_{1}$ be the parasitic capacitance of the intermediate node closest to the output
- assuming a pulldown chain of $N$ series of connected nmos transistors, then
	- if $C_L \lt (N-1)\frac{C_1}2$, then the overall delay can be reduced by decreasing the size of the nmos transistor closest to the output node
	- this can be iteratively applied to other transistors in pulldown chain → graded sizing of all nmos devices
#### Example
Consider the domino cmos AND2 gate, where $C_1=C_2=0.5pF$
<Image src="/attachments/IMG-20231211155904.png" alt="Image"/>
The following signals were given into the circuit
<Image src="/attachments/IMG-20231211155958-1.png" alt="Image"/>
First, operation of circuit with 1 pmos is tested; since $C_1=C_2$, we expect that charge-sharing will cause erroneous output values. As shown below, even when $V_B$ is low, $V_{out}$ does not go to 0.
<Image src="/attachments/IMG-20231211155958-2.png" alt="Image"/>
Next, consider the case where an additional pmos percharge transistor is connected between $V_{DD}$ and the intermediate node. Both pmos transistors conduct during precharge and charge up the node capacitance to the same voltage level so that no charge sharing can occur. This leads to the correct graph shown below.
<Image src="/attachments/IMG-20231211155958-3.png" alt="Image"/>
