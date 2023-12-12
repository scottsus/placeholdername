---
lecture: 12.2
sidebar_position: 32
date: 2023-11-08
topics:
  - timing
  - latches
---
## SPICE
- Simulation Program with Integrated Circuit Emphasis (SPICE)
	- Electronics Research Laboratory at UC Berkeley
- basically a general purpose analog circuit simulator
- used in IC and board-level design integrity check of circuit designs and prediction of circuit behavior
- description of circuit elements and connections by netlists
	- netlists translated into nonlinear differential algebraic equations
- solving by implicit integration methods, Newton’s method, sparse matrix techniques
### HSPICE
- has superior convergence, accurate modeling
### Basic Netlist Structure
- Parameters
	- .param Wn=2u L=0.6u
	- .param Wp=2Wn
- Power supplies and sources
	- V1 VDD 0 5
	- VPULSE VIN 0 PULSE 0 5 2N 2N 2N 98N 200N
- Actual circuit topology
	- M1 VOUT VIN VDD VDD pch Wp L M=1
	- M2 VOUT VIN GND GND nch Wn L
- Analysis statement
	- .TRAN 1n 300n
- Output control statements
	- .OPTION POST
	- .PRINT V(VIN) V(VOUT)
- Library
	- .LIB ‘AMS.lib’ nominal
	- .END
## Documentation
### Input/Output Files & Suffixes
- Recommended Formats
- Input Controls
	- .OPTION, .PARAM, .ALTER, .MODEL, .LIB
- Output Controls
	- .PRINT, .MEASURE
### Power Sources
- Independent Sources
	- DC, AC
- Transient Analysis: Source Functions
	- Trapezoidal pulse (PULSE), Sinusoidal (SIN), Exponential (EXP), Piecewise Linear (PWL), etc
### Analysis
- DC Analysis
	- .DC, .OP, .TF
- AC Analysis
	- .AC
- Transient Analysis
	- .TRAN
