---
lecture: 13.1
sidebar_position: 28
date: 2023-11-20
topics:
  - domino
  - NORA
---
import Image from '@site/src/components/Image'
import DisplayFlex from '@site/src/components/DisplayFlex'

## NORA CMOS Logic
- otherwise known as NP-Domino logic
- Idea: dynamic logic stages that also use pmos transistors
	1. when clock is low:
		nmos output nodes are precharged to $V_{DD}$ through pmos precharge devices
		pmos output nodes are pre-discharged to 0V through nmos discharge transistor
	2. when clock low → high:
		all cascaded nmos and pmos logic stages evaluate one after another
	<Image src="/attachments/IMG-20231211160042.png" alt="Image"/>
- example
	<Image src="/attachments/IMG-20231211160042-1.png" alt="Image"/>
- Advantages:
	- static cmos inverter not required at output of every dynamic logic stage
		- pmos handles 1 → 0, nmos handles 0 → 1
	- instead of dynamic → static → dynamic → static, we get dynamic → dynamic → dynamic
	- allows **pipelined system architecture**
### Zipper CMOS Circuits
- zipper technique overcomes dynamic charge sharing & soft-node leakage problems
- identical to NORA CMOS, but requires generation of slightly different clock signals for precharge/discharge transistors and for pullup/pulldown transistors
	- signal $\chi=V_{DD}-V_{T0,p}$
	<Image src="/attachments/IMG-20231211155905.png" alt="Image"/>
- clock signals allow precharge/discharge transistors to remain in weak conduction or near cutoff during eval, compensating for charge leakage & charge sharing problems
### True Signal-Phase Clock (TSPC) Dynamic CMOS
- TSPC uses 1 clock, never inverted → no clock skew
- higher clock frequency ⏰👍
	<Image src="/attachments/IMG-20231211160042-2.png" alt="Image"/>
- Consider the circuit shown above:
	- when clock is low, output of N-block is precharged to $V_{DD}$
	- when clock low → high, logic stage output evaluated, output latch generates valid output level
	- when clock is high, P-block pre-discharges and evaluates when clock is low
- compared to NORA CMOS, we need 2 more transistors per stage, but ability to operate with a true single-phase clock signal is attractive

