---
lecture: 12.1
sidebar_position: 10
date: 2023-11-06
topics:
  - sequential
  - latch
  - flip-flop
---
import Image from '@site/src/components/Image'

### Sequential Logic Circuits
- output levels of a **[[combination circuit]]** at any time are directly determined as boolean functions of the applied input variables
	- combinational logic cannot store previous event or display output behavior dependent on previously applied inputs
	- these are called *non-regenerative* circuits as there is no feedback relationship between input & output
- the other class of logic circuits are **[[sequential circuits]]**, in which the output is determined by present as well as previous inputs
- 3 types of sequential circuits: *bistable*, *monostable*, *astable*
## Bistable Circuits
- consider the following example
	<Image src="/static/attachments/IMG-20231207175829.png" width="300px" alt="Image"/>
- this circuit consists of 2 identical cross-coupled inverters
	- output of inverter 1 is input of inverter 2, and vice versa
	- in other words:
		$\\ \quad v_{o1} = v_{i2}$
		$\\ \quad v_{o_{2}}=v_{i_{1}}$
- to characterize this circuit, we plot the voltage transfer characteristics (VTC's) of both inverters using the same pair of axes
	- the 2 VTC's, which can be thought of as curves, intersect at 3 points
		<Image src="/static/attachments/IMG-20231207175854.png" width="300px" alt="Image"/>
	- each intersection is an *operating point*, and there are 2 stable and 1 unstable operating points → hence the name *bistable*
		- the unstable region in red is also called the <span style={{ color: '#f55656' }}>metastable region</span>
### Bistable Latch
- the simple 2-inverter circuit can store a state, but is unable to change its state upon application from an external agent
- Solution: bistable latch shown below
	<Image src="/attachments/IMG-20231207175914.png"/>
	- this circuit consists of 2 NOR gates connected together
		- notice the PUN with 2 pmos in series and PDN with 2 nmos in parallel
- this SR latch has 2 complementary outputs $Q$ and $Q'$
	- *set state*: $Q=1, Q'=0$
	- *reset state*: $Q=0, Q'=1$
	<Image src="/attachments/IMG-20231207175926.png"/>
- Truth table

| S   | R   | $Q_{n+1}$ | $Q_{n+1}'$ | Operation   |
| --- | --- | --------- | ---------- | ----------- |
| 0   | 0   | $Q_{n}$   | $Q_{n}'$   | hold        |
| 1   | 0   | 1         | 0          | set         |
| 0   | 1   | 0         | 1          | reset       |
| 1   | 1   | 0         | 0          | not allowed |

- operation of the SR latch can be examined in more detail by considering the operation modes of the 4 nmos transistors $M_{1}-M_{4}$

| S        | R        | $Q_{n+1}$ | $Q_{n+1}'$ | Operation                                       |
| -------- | -------- | --------- | ---------- | ----------------------------------------------- |
| $V_{OH}$ | $V_{OL}$ | $V_{OH}$  | $V_{OL}$   | $M_{1}$ and $M_{2}$ on, $M_{3}$ and $M_{4}$ off |
| $V_{OL}$ | $V_{OH}$ | $V_{OL}$  | $V_{OH}$   | $M_{1}$ and $M_{2}$ off, $M_{3}$ and $M_{4}$ on |
| $V_{OL}$ | $V_{OL}$ | $V_{OH}$  | $V_{OL}$   | $M_{1}$ and $M_{4}$ off, hold prev state        |
| $V_{OL}$ | $V_{OL}$ | $V_{OL}$  | $V_{OH}$   | $M_{1}$ and $M_{4}$ off, hold prev state        | 

- when $S$ and $R$ are both low, the inputs to $M_{2}$ and $M_{3}$ are $Q$ and $Q’$ respectively, allowing them to hold the previous states
### NOR-Based SR Bistable using Depletion Load NMOS
- *SR*: Set-Reset
- a NOR-based SR latch can also be implemented (instead of INV) → using nmos instead of cmos
	<Image src="/static/attachments/IMG-20231207175940.png" width="500px" alt="Image"/>
- from a logic pov, this is identical to cmos SR latch
	- but cmos implementation is better due to power dissipation and noise margin
### NAND-Based SR Bistable using Depletion Load NMOS
- additionally, a NAND-based SR latch can also be implemented
	<Image src="/static/attachments/IMG-20231207175954.png" width="500px" alt="Image"/>
- inputs are **active low**

| S | R | $Q_{n+1}$ | $Q_{n+1}'$ | Operation |
| --- | --- | --------- | ---------- | ----------- |
| 0 | 0 | 1 | 1 | not allowed |
| 0 | 1 | 1 | 0 | set |
| 1 | 0 | 0 | 1 | reset |
| 1 | 1 | $Q_{n}$ | $Q_{n}'$ | hold |

- compare this with NOR-based SR latch which has **active high** inputs
## Latch and Flip-Flop Circuits
- now we consider a *clocked* bistable or a *latch*
- all SR latches so far are asynchronous
	- latch response can be controlled by adding a gating clock signal to the circuit
	- outputs respond to input levels only during the active period of the clock pulse
- clock pulse assumed to be a periodic square waveform, simultaneously applied to all clocked logic gates in the system
### NOR-Based SR Latch
- AND → NOR gates
	<Image src="/static/attachments/IMG-20231207180008.png" width="450px" alt="Image"/>
- when CK=0, inputs have no influence on outputs
- when CK=1, S and R are permitted to reach SR latch
- Operation
	<Image src="/attachments/IMG-20231207180019.png"/>
- <span style={{ color: '#f55656' }}>Problem:</span> this circuit is *level sensitive*, meaning when CK=1, any changes in $S$ and $R$ will be reflected onto the outputs
- even a narrow glitch occuring during an active clock phase can set or reset the latch
### AOI-Based Implementation
- *AOI*: AND-OR-INVERT
	<Image src="/attachments/IMG-20231207180029.png"/>
### NAND-Based SR Latch
- OR → NAND gates
	<Image src="/static/attachments/IMG-20231207180039.png" width="450px" alt="Image"/>
	- both input signals & clock are active low
	- implementation possible using the OAI structure
#### A different implementation of the NAND-based SR latch
- NAND → NAND gates
	<Image src="/static/attachments/IMG-20231207180055.png" width="450px" alt="Image"/>
- we can also think of it as
	<Image src="/static/attachments/IMG-20231207180109.png" width="450px" alt="Image"/>
- in this case, both input signals & clock are active high
- latch preserves its state as long as CK=0
- <span style={{ color: '#f56332' }}>Drawback:</span> higher transistor count than active low version
### JK Latch
- all the latch circuits above suffer from the common problem of a *not allowed* input combination
	- their states become indeterminate when both $S$ and $R$ are active at the same time
- this problem can be solved by adding 2 feedback lines from outputs to inputs
	<Image src="/static/attachments/IMG-20231207180121.png" width="450px" alt="Image"/>
	- when CK=1 and $J=K=1$, outputs will simply toggle
#### All-NAND implementation of JK latch
- all NAND gates
	<!-- <Image src="/attachments/📖%Spelling%Correction%&%Statistical%Machine%Translation_jpg_6.png"/> -->
#### NOR-based JK latch with AOI realization
- from [[Sequential Logic Design Part I#AOI-Based Implementation]]
	<Image src="/attachments/IMG-20231207180134.png"/>
- simplified to
	<Image src="/static/attachments/IMG-20231207180145.png" width="400px" alt="Image"/>
#### A timing problem in JK latch
- we mentioned that there is no *not allowed* input combination for a JK latch
- however in the case $J=K=1$, the output will oscillate continuously until either one of inputs or clock becomes 0
- to prevent this undesirable timing problem, the clock pulse width must be made smaller than the propagation delay of the JK latch circuit
	- this means the clock signal must go low before the output level has the opportunity to switch again, preventing the uncontrolled oscillation of the output
		<Image src="/attachments/IMG-20231207180208.png"/>
- this clock constraint is difficult to satisfy for most practical applications
	- but the idea of solving the *not allowed* case and having the toggling output is still good
	- we’ll develop this idea to build the JK FF
## Master Slave FF
- an intermediate to the next idea, we can solve most of the previously-mentioned timing limitations in JK latches by cascading 2 latch stages
- *master*: input latch, *slave*: output latch
	<Image src="/attachments/IMG-20231207180231.png"/>
	1. when CK=1, $J$ and $K$ can enter the FF, master outputs set
	2. when CK=0
		- master inactive, slave active
		- slave takes master outputs
	3. when $J=K=1$, circuit toggles
		- but because only 1 stage is active at any given time, there is **no toggling**
- essentially, we’re constructing an *edge-triggered* FF by combining 2 level sensitive ones
### NOR-Based Realization of JK Master-Slave FF
- AND → NOR → AND → NOR
	<Image src="/attachments/IMG-20231207180243.png"/>
- <span style={{ color: '#f55656' }}>1’s Catching Problem:</span> while CK=1, a narrow spike or *glitch* in 1 of the inputs, say in the $J$ line, may set/reset the master latch and cause an unwanted state transition in master latch → propagating to slave in the next phase
## D Latch
- we return to [[Sequential Logic Design Part I#NOR-Based SR Latch]], where we modify it to obtain a D Latch
	- instead of $S$ and $R$ signals, we have a single $D$ signal
	<Image src="/static/attachments/IMG-20231207180258.png" width="450px" alt="Image"/>
	- when CK=1, $Q=D$
	- when CK=0, $Q$ preserves its state
	- effectively, CK input acts as an enable signal for $D$ to be accepted
### Transmission Gates (TG) for Latches & FFs
- direct cmos implementation of clocked JK latch & JK master-slave FFs require a large amount of transistors → consider TGs
### CMOS TG implementation of D latch
- using just TG’s
	<Image src="/static/attachments/IMG-20231207180309.png" width="450px" alt="Image"/>
	- when CK=1
		- $D$ → INV1 → INV2 → $Q$ as expected
			- it’s also *trapped* between the 2 inverters
		- TG2 = high impedence, so $D$ doesn’t flow to TG2
	- when CK=0
		- TG1 = high impedence
		- *trapped value* → INV2 → TG2 → INV1 → INV2 → Q
	- <span style={{ color: '#3291f5' }}>note:</span> TGs are bidirectional, and logic can flow from both left → right & right → left
