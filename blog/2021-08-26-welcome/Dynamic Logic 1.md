## Dynamic Pass Transistor Circuits
- consider the generalized view of a multistage synchronous circuit shown below
	![Image](/attachments/IMG-20231207180653.png|550)
- to drive the pass transistors, 2 non-overlapping clock signals are used
	- this is known as *2-phase clocking*
	![Image](/attachments/IMG-20231207180709.png|400)
### Depletion Load Dynamic Shift Register
- Idea: we can make a sequence of FFs to store a few bits of data to form a register
	- the *shift* implies bits are moved from one FF to the next
- consider this next multistage synchronous circuit
	![Image](/attachments/IMG-20231207180734.png)
- during the active phase of $\phi_{1}$, $V_{in}$ is transferred into $C_{in1}$ → valid output voltage is the inverse of input $V_{in}$
- when $\phi_2$ becomes active during the next phase, the output voltage level from stage 1 is transferred into the 2nd stage input capacitance $C_{in2}$ → valid output voltage of stage 2 is determined
	- during this time, $C_{in1}$ retains its previous level via charge storage
	- when $\phi_1$ becomes active again, the original data bit written into the register during the previous cycle is transferred into stage 3, and stage 1 can accept the next data bit
- for every active phase, a clock $\frac12$ period must be long enough to allow input cap $C_{in}$ to charge up or down, and the logic level to propagate to the output by charging $C_{out}$
### Dynamic 2-Stage Circuit
- the same operation principle used in the shift register above is used for synchronous depletion nmos logic 1
	![Image](/attachments/IMG-20231207180744.png)
- note: to guarantee correct logic levels are propagated during each active clock cycle, the clock $\frac12$ period length must be longer than the largest single stage propagation delay
## Dynamic CMOS Logic
- significantly reduces number of transistors used to implement any logic function (compared to CMOS) with 0 static power consumption
- Idea:
	1. *precharge* output node capacitance
	2. *evaluating* output level according to applied inputs
- by having the precharging phase, this circuit is faster because we no longer need the PUN ⚡️
- Suppose we have a dynamic cmos logic gate implementing the complex boolean function $F=(A_1A_2A_3+B_1B_2)'$
	![Image](/attachments/IMG-20231207180754.png|400)
- then the graph can be modeled as
	![Image](/attachments/IMG-20231207180816.png|300)
- when clock is low (precharge phase), $M_p$ is conducting while $M_e$ is off
	→ $V_{out}=V_{DD}$
- when clock signal is high (evaluation phase), $M_p$ is off while $M_e$ is on
	→ $V_{out}$ depends on input voltage levels
	1. if $F$ is true, then $V_{out}$ will be pulled to GND
	2. say A1 or B1 is 0, then $V_{out}$ will retain its previous capacitance
### Cascading Dynamic CMOS Logic
- during the precharging phase, $V_{out1}$ and $V_{out2}$ are pulled up, and external inputs are applied
- assume input variables of stage 1 are such that $V_{out1}$ will drop to logic 0 during the eval phase
	![Image](/attachments/IMG-20231207180836.png|450)
- <span style={{ color: '#f55656' }}>Problem:</span> there is an issue when dynamic cmos is cascaded
	1. when eval phase begins, $V_{out1}$ and $V_{out2}$ are initially logic 1 ($V_{out1}$ eventually drops to the correct logic level after a certain time delay)
	2. during this transition, $V_{out1}$ is suggesting $V_{out2}$ to be low at first → $V_{out2}$ at the end of the eval phase may be erroneously low
	3. although $V_{out1}$ eventually settles to correct value, after stored charge is drained, correction of $V_{out2}$ is not possible without PUN
		![Image](/attachments/IMG-20231207180852.png|350)
## Domino CMOS Logic
- a dynamic cmos logic stage must be cascaded with a static cmos inverter stage
	1. during the precharge stage, $V_{out1}$ is precharged to logic 1 → force $V_{out2}$ to go to 0
	2. during the eval phase, $V_{out1}$ either discharged or remains high → $V_{out2}$ charges to high (0 → 1 transition) or remains low
	3. importantly, a 0 and 0 → 1 for $V_{out2}$ will not result in error for next stage - we are effectively disallowing 1 → 0 transitions
- recall this was our diagram for cascading cmos
	![Image](/attachments/IMG-20231207180915.png|400)
- essentially, domino structure solves the cascading problem by <span style={{ color: '#73e265' }}>removing the 1 → 0 transition</span> of the next nmos input
	- the easiest way to do this is to add a simple inverter after each stage
	![Image](/attachments/IMG-20231207180930.png|450)
- moreover, domino cmos gates allow significant reduction in number of transistors required to realize any complex boolean function
	![Image](/attachments/IMG-20231207180947.png|400)
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
	![Image](/attachments/IMG-20231207181003.png)
- disadvantage: to build NOR, we also need to build a NAND (inefficient in domino)
### Charge Sharing
- consider the following circuit
	![Image](/attachments/IMG-20231207181013.png|450)
	- $C_2$ is comparable in size to $C_1$
	- all inputs are initially low, $C_2=0V$
	- during precharge, $C_1$ charged up to $V_{DD}$
	- during eval, if input signal to nmos (in the box) switches from 0 → 1, then the charge from $C_1$ will now be shared with $C_2$, leading to a *charge-sharing phenomenon*
	- the output node voltage after sharing is given by
		$\\ \quad \frac{V_{DD}}{1+C_{2}/C_{1}}$
- <span style={{ color: '#f55656' }}>Problem:</span> if $C_1=C_2$, this may lead to erroneous $V_{out}$
### Preventing the Charge Sharing Problem
- Idea 1: add a weak pmos pullup device with small $W/L$ to dynamic cmos stage output, essentially forcing a high $V_x$ unless there is a strong pulldown path between $V_x$ and ground
	![Image](/attachments/IMG-20231207181026.png|450)
	1. as $V_x$ degrades → $V_{DS}\neq0$ → pmos turns on
	2. $V_x$ pulled back up to $V_{DD}$
- Idea 2: separate pmos transistors to precharge all intermediate nodes in nmos pulldown tree
	![Image](/attachments/IMG-20231207181042.png|450)
	- multiple percharge transistors also enables us to use precharged intermediate nodes as resources for additional outputs (multiple-output domino)
### Multiple-Output Domino
- consider the following realization of 4 boolean functions of 9 variables using a single domino cmos logic gate
	![Image](/attachments/IMG-20231207181056.png)
- comparing this with
	1. 4 separate standard cmos logic gates
	2. 4 separate single-output domino cmos circuits
- this is much more compact!
### Transistor Sizing
- adjusting nmos transistor sizes in pulldown path can reduce discharge time
- recall that the best performance is obtained with a *graded sizing* of nmos transistors in series
	- similarly, bottom-most transistor should be sized the largest
	![Image](/attachments/IMG-20231207181106.png)
- let
	$\\ \quad C_L$ be the load capacitance
	$\\ \quad C_{1}$ be the parasitic capacitance of the intermediate node closest to the output
- assuming a pulldown chain of $N$ series of connected nmos transistors, then
	- if $C_L \lt (N-1)\frac{C_1}2$, then the overall delay can be reduced by decreasing the size of the nmos transistor closest to the output node
	- this can be iteratively applied to other transistors in pulldown chain → graded sizing of all nmos devices
#### Example
Consider the domino cmos AND2 gate, where $C_1=C_2=0.5pF$
![Image](/attachments/IMG-20231207181115.png|450)
The following signals were given into the circuit
![Image](/attachments/IMG-20231207181133.png|450)
First, operation of circuit with 1 pmos is tested; since $C_1=C_2$, we expect that charge-sharing will cause erroneous output values. As shown below, even when $V_B$ is low, $V_{out}$ does not go to 0.
![Image](/attachments/IMG-20231207181149.png|450)
Next, consider the case where an additional pmos percharge transistor is connected between $V_{DD}$ and the intermediate node. Both pmos transistors conduct during precharge and charge up the node capacitance to the same voltage level so that no charge sharing can occur. This leads to the correct graph shown below.
![Image](/attachments/IMG-20231207181207.png|450)
### NORA CMOS Logic
- otherwise known as NP-Domino logic
- Idea: dynamic logic stages that also use pmos transistors
	1. when clock is low:
		nmos output nodes are precharged to $V_{DD}$ through pmos precharge devices
		pmos output nodes are pre-discharged to 0V through nmos discharge transistor
	2. when clock low → high:
		all cascaded nmos and pmos logic stages evaluate one after another
	![Image](/attachments/IMG-20231207181224.png)
- example
	![Image](/attachments/IMG-20231207181239.png)
- Advantages:
	- static cmos inverter not required at output of every dynamic logic stage
		- pmos handles 1 → 0, nmos handles 0 → 1
	- instead of dynamic → static → dynamic → static, we get dynamic → dynamic → dynamic
	- allows **pipelined system architecture**
### Zipper CMOS Circuits
- zipper technique overcomes dynamic charge sharing & soft-node leakage problems
- identical to NORA CMOS, but requires generation of slightly different clock signals for precharge/discharge transistors and for pullup/pulldown transistors
	- signal $\chi=V_{DD}-V_{T0,p}$
	![Image](/attachments/IMG-20231207181251.png|450)
- clock signals allow precharge/discharge transistors to remain in weak conduction or near cutoff during eval, compensating for charge leakage & charge sharing problems
### True Signal-Phase Clock (TSPC) Dynamic CMOS
- TSPC uses 1 clock, never inverted → no clock skew
- higher clock frequency ⏰👍
	![Image](/attachments/IMG-20231207181304.png)
- Consider the circuit shown above:
	- when clock is low, output of N-block is precharged to $V_{DD}$
	- when clock low → high, logic stage output evaluated, output latch generates valid output level
	- when clock is high, P-block pre-discharges and evaluates when clock is low
- compared to NORA CMOS, we need 2 more transistors per stage, but ability to operate with a true single-phase clock signal is attractive
		


