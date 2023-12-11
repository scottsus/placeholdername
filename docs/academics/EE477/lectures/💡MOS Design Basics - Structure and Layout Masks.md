---
lecture: 3.2
sidebar_position: 6
date: 2023-09-06
topics:
  - A
  - B
  - C
---
import Image from '@site/src/components/Image'

- nmos: n-type source and drain, p-type substrate    
- pmos: p-type source and drain, n-type substrate
- cmos example
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/ff77f78c-19ae-4d67-955c-0c2b6cde0699/Untitled.png)
    

### Inverter Layout

- ********************2 Possible Configurations********************

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/7694c52d-e155-4e7b-a888-53f33d5fff3b/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/ff99ce80-a4bf-4b14-8561-d031dc8cee56/Untitled.png)

- **********************Layout View**********************
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/b9e3d116-07bb-4096-9272-cfe6ce4befea/Untitled.png)
    

### NAND Schematic and Layout

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/21948cb9-78f0-4920-9cb7-52557fa36f16/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/b5ec48c2-32ce-4293-bce1-bc77dbcfaa01/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/ce2972d7-e733-404d-96c1-3de15b1f7ffe/Untitled.png)

### NOR Schematic and Layout

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/408d3b3e-0cef-415c-a44e-aa0124da4845/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/32dd34f3-56ad-46ed-80f5-a4a6daf99e8b/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/aa11c2b1-8447-4802-ad54-0b5cbef5ad8a/Untitled.png)

## Complex Gates

- consider the following boolean function: $Z = \overline {A(D+E)+BC}$
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/09c90485-d979-466e-92be-2cd2911de870/Untitled.png)
    
- all parallel connections in nmos PDN will correspond to a series connection in pmos PUN
    

### Complex CMOS Logic Gates

- a series connection in PDN correspond to parallel connections in PUN
    
    1. each driver transistor in PDN is represented by an edge
        - each internal node is represented by a vertex in PDN
    2. a new vertex is created within each confined area in PDN
        - neighboring vertices are connected by edges which cross each edge in PDN only once
        - this graph represents PUN
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/bb1298b5-9143-4cc5-9d3e-57fa64900f88/Untitled.png)
    
- the number of diffusion breaks can be minimized by changing ordering of polysilicon columns
    
- simple method for finding optimum gate ordering is the ********************Euler-path******************** approach
    
    - find a common Euler path for both PDN and PUN graphs
    - polysilicon columns can be arranged according to the sequence in Euler path
- an easier method is just ******************************trial and error****************************** until we find a path that satisfied both PUN and PDN
    
- diffusion will be unbroken if identically labeled Euler paths can be found for p and n trees
    
- Optimize stick-diagram layout of complex CMOS logic gate
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/301897bf-5a14-4124-a931-1599cc4d8292/Untitled.png)
    

## CMOS Full Adder Circuit

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/16ccaa11-a99e-4d74-a81a-0f3f3cac8e9a/Untitled.png)

### Sum and $c_{out}$ circuit for a 1-bit FA

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/fb02626d-02b8-459a-aca5-0490071d500a/Untitled.png)

### FA Layout

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/bfc12e47-eb48-4e05-b5c4-7edcd96503b5/Untitled.png)

### Performance-Optimized, Compact Mask Layout

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/e59a450d-9816-42c8-9691-24f530a617a4/Untitled.png)

### FA Waveform Extraction

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/c3f14b39-a482-4390-bd07-aedf01dd2ded/Untitled.png)

### Ripple Carry Adder (RCA)

- simplest FA circuit can be constructed by a cascade of FA’s
    - each adder performs a 2-bit addition → produces corresponding sum bit → passes $c_{out}$
- speed of RCA limited by delay of carry bits ripplying through carry chain
- path from $c_0$ to $s_7$ is the ******critical path******