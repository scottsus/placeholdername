---
lecture: 12.2
date: 2023-11-08
topics:
  - timing
  - latches
---
import Image from '@site/src/components/Image'

## Setup and Hold Times
- *setup time $t_{setup}$*: min time data <span style={{ color: '#f55656' }}>before</span> the clock edge the input data must be stable
- *hold time $t_{hold}$*: min time <span style={{ color: '#f55656' }}>after</span> clock edge which the data must be stable
	![Image](/attachments/IMG-20231207175458.png)
### Metastability
- if change of data occurs too closely to the clock edge, the FF may go to an unstable/metastable state
	- may result in faulty output
- this behavior enforced in latches as well
## D Latch
### Tristate Inverter
- a type of inverter with 3 output states: 1, 0, Z
### Implementation
- 2 tristate gates and 1 inverter
	![Image](/attachments/IMG-20231207175528.png)
	- when CK=1, TINV2=Z, TINV1=$D$, $D=Q$
	- when CK=0, TINV1=Z, TINV2=*mem*, preserving its state
## Transition-Triggered Monostable Circuit
- type of electronic circuit used to generate a single output pulse of a fixed duration coming from an input signal
- *monostable*: circuit has only 1 stable state, other states (singular actually) is temporary
	![Image](/attachments/IMG-20231207175550.png)
### Logic Gate-Based Monostable Trigger
![Image](/attachments/IMG-20231207175603.png)
### DFF with Asynchronous Reset
![Image](/attachments/IMG-20231207175622.png)
## Clock-to-Q Delay and Timing Constraints
![Image](/attachments/IMG-20231207175634.png)
<Image src="/attachments/IMG-20231207175644.png" width="350px"/>
### Hold Time Violation Example
- $D$ is not held for long enough
- below is an example of a *Write-after-Write* hazard
	<Image src="/attachments/IMG-20231207175702.png" width="500px"/>
	- new data stored instead of previous data
### Setup Time Violation Example
- delay in combinational logic is larger than clock time cycle
- below is an example of a *Read-before-Write* hazard
	<Image src="/attachments/IMG-20231207175725.png" width="500px"/>
	- data arrives late at register $B$, and old data is retained instead of latching new data
## Schmitt Trigger Buffer Circuit
- regenerative
	<Image src="/attachments/IMG-20231207175738.png" width="200px"/>
- has an inverter-like VTC, but with 2 different logic threshold voltages for increasing and decreasing input signals
	<Image src="/attachments/IMG-20231207175751.png" width="300px"/>
- can be utilized for detection of low-to-high and high-to-low switching events in noisy environments
### Noise Suppression using Schmitt Trigger
![Image](/attachments/IMG-20231207175803.png)
