## [VNC Server](https://learn-us-east-1-prod-fleet02-xythos.content.blackboardcdn.com/5fd94affdac6c/32931240?X-Blackboard-S3-Bucket=learn-us-east-1-prod-fleet01-xythos&X-Blackboard-Expiration=1693936800000&X-Blackboard-Signature=RWcV26vz%2FdorkF%2FylysyTB3T7%2Fyl%2FyistU7Y09eFWzo%3D&X-Blackboard-Client-Id=100775&X-Blackboard-S3-Region=us-east-1&response-cache-control=private%2C%20max-age%3D21600&response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%27EE477_Lab_Environment_Setup.pdf&response-content-type=application%2Fpdf&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIFlkqr6uVY1mEUe3E7Sa%2FLY5wSXsHr7zSaaDSsZqqGDjAiEAtiWmaTnysiY8LeZcP94BtLNpSd2UjEly83nxaoRU76gqtAUIXRADGgw2MzU1Njc5MjQxODMiDHhAf0cN87%2BsquN8QiqRBe3DGhSSWEHm3kwgiZjnmxavBVyCoPm%2BGQGZ60S38YOEkzk1pj1O5XxjHk85os7Ttp2C8UM%2BJVNuOXXgCkq2nF9xL9l9zLMtXH55KLEfKTcyPNvyYB6SRbMqSkEL6l8ct0nV7J1brc81mHUpT3deLirtA9RVUZJs47Yy%2B7mBB%2BBQKJDWDfCeIQiiZsBbZp8FmxSlgvLZPWt40ICKna16al2HkCt7syTRMJGwGCnFusjjl%2Fry5RVUaHRN5mxRi%2FhnWc%2BEI3ldPWtyozDQXHoJd9cYft%2FsU08Fv%2FGuneGKyoNYFvJoQMgGnN%2BZvSBWRArYUwgFJiJnLE9ZzQq4yOdVFRNuylVPYWzuu2GXd%2BKEqUk3Zv7IfF5WykYRBxFK1aaJrYO84TBOihOtFDn9kR%2BtIzEFn9jm2YbzO%2BeJXqfjFSlpwrqP1zi90dn02jcJLYuQuBlqSJemh1j3ByGo%2BK0ka1ZMcAiO6PtwLaz0nyYH3m0D3QOHeNHMNOjona7NCDeIoPAl%2BfCvd7RlaftUubV1%2FmJUKFnqE6krTp66rerlMDQHhC37ME0R1o1sNrTPJyna0urNo5cxA2arT70aPEddWq6aCexJx0FtU%2BYXCY5nnV7fTAKlktldMqxKM98PwWolHcqULWpeFeI70qvAWs%2Fm3Viv%2FvAbiK%2Fz7MNzP0CT%2FL1KVskRzgcLiXxgpagi8Kw6tn3ksBxjYCBc2%2BFYaAkWsfN3QtbWhvrlf8N0TDuUYxOevV2i0RvPpvLXppfB4gUf1fiSpVwMRETrM1CNec7xBY8t3h7Xa5Lzm0bY0D65%2FZYNv0F24pwzOi3j%2BWdWREt1%2FZz34q7Mj%2FJCncJ%2B4bZubiyyPzhDumewYC41ViQV0HWBnDDlqdynBjqxAam6CbNDFlZx645dKwiLYFmRhEJUNWaPBOydE6U8oERq19L1TJCVAFBDYLRHFwpsOynMxZwBwfJs6K76fHG0VYbTt3aSfht5S6tiiAN%2BUwh2Xm1GtBKDj2yJhBbJLiFioJHSGLCHWCzDHmQ4Jq3%2FtmGLPDxljp%2F%2FAZKzDQPFk7G2C%2FCOWL8VHp6vp7nhjicC8Gff3W%2FVGpvLIymbPyJOjYchW10dC7PzVz02nqtk8AxZqw%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230905T120000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=ASIAZH6WM4PL5LUWL7WE%2F20230905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b20370ddc12e741cf48b9aa6bb5ab2bb5690ae72a70c24c67d667c2b1524606c)
1. Access instance
    `ssh scottsus@viterbi-scf2.usc.edu`
2. Create VNC server instance
    `vncserver -geometry 1920x1080`
    `vncserver -list`
    `vncserver -kill :10004`
3. Setup ssh tunneling
    `ssh -L 15004:localhost:15004 -N -f -l scottsus viterbi-scf2.usc.edu`
## [Cadence Virtuoso](https://learn-us-east-1-prod-fleet02-xythos.content.blackboardcdn.com/5fd94affdac6c/18930628?X-Blackboard-S3-Bucket=learn-us-east-1-prod-fleet01-xythos&X-Blackboard-Expiration=1693926000000&X-Blackboard-Signature=Lk7Wh11gO%2FaUV8wg6WmT2Y%2F2bEdeYs4FZoSxYuy51cc%3D&X-Blackboard-Client-Id=100775&X-Blackboard-S3-Region=us-east-1&response-cache-control=private%2C%20max-age%3D21600&response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%27Additional%2520Cadence%2520Virtuoso%2520Guide%252845%2520nm%2529.pdf&response-content-type=application%2Fpdf&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIF0U%2FasEOJJ9hSZ0JhI5pPq2f0g%2BsFgF90xVZwDE%2B85%2FAiAHGXov889nthqWYWDvx7IWMZdUf5AK4HnHtL%2BaoDeu1iqzBQhbEAMaDDYzNTU2NzkyNDE4MyIMsb4OtBfUp1XXjnLAKpAFjjZ2NeUMqC9ExmlvRrVbH9gTWrvXx1oiEoOH%2BPiVL%2FlVo9wlqaoZPX9AKucINZz%2Fe0QPAsJOKFe6Ui6sxPubLAs9cR9Mvq36RliBvNEzW%2BphkfqEkFheClvBBMaz8K134u3jjzlCjZMskcvN6MJDNxdk3Zo0VsQa96Dfi5SDWYp77iapcSAVucEhTSvOdv%2FE6UHiBsbZLJWs5Y5JEGUTdsa72%2BtkWDbChiDTPzEhz%2BpXPblOfaYRyUUasRW8ZthkjM%2BnP7%2Fzu2fFTf9bajhGSXx9dX7EcVBjWynIh7AyKTENS2LVu%2FsjF2DyXrAYvn30k5vrxNOwIo3g%2BltyvrcyN4J1qXqJ9WvMVqnfZslwCOcu2LsP4nyCSn2e9AHahgeu6Hf6ZxZOqN%2F8ZvI5Sb6GnBqMz7HsH1oEF8NawjceqAyE6%2FdXcy7VtCxPnWgA2i9h1XgcCFT5BJ3gnGMUXsAaADJkG%2BQu%2FKawHR%2Farfw4%2FFFNNYCjH8kuiDSyu65Fd1TQbLVtvDIm%2FRqcy%2BP1RGMXKaqFWneC2Gn8M2yf2N4qNvPZU3OLGysQ%2BYDL2rwXkdmSI1s5XlJUk9FZma92oxM%2BPGV%2FSnoc5TKrTbVHHsNWrWK74Pa8z2qbUpF1fsBWriD4TFkKrHoDJh%2F%2FoaIABwQ8fiwy2v%2FHSptAnRjUQNbBiVqXeoyYAwMBBrdARFHXuI4IorCB4lOnymVqNljWdb7GoMr2PKTwHaneg4SMNvdMn6AC3Z8%2Fahv%2Ff2Xqr3zWllVVj6H5GVsWRH%2FQzJ8e1VEMG4Xs4TFvI2nbpDXqf6dYttofHfawZzE%2BoLb54G%2FZFGzj4oCNnEeBHoDuvefkjnrqdEfp%2FGraFKj3rnIhf1Er6qMwkujbpwY6sgEObAkcto4GqEKhrmFDUWXtgt7Mdhtc9dt2M1wzI0W5c7qd3pRRq7qYzQ73PhVyml6MjF6IJGC4ky4CSwz%2Fe4jcTxEz6rDB3Oo7SF46qu%2FjwigTi8cYQ4lfrMVh5W2eck6XFe1Mqs5ZbqWnSK%2B8ouvOPRY7Fp8RXWMmndUpgITl8RqCuXBkeyo1WBrCD5GFvNnvAdWbBg4oQgrsEbZWp0M1QVQ63ya4BNfAaVUdXyWLbSf5&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230905T090000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=ASIAZH6WM4PLSRXEF5G3%2F20230905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=e3ade48142ee44bc2f81918713918aef3a09b154b7ebd13e679c791078070859)
### Launching
1. Source virtuoso
    `source setup_ee477_ee577a_v2102.csh`
2. Launch virtuoso
    `cd work_gpdk045`
    `virtuoso &`
### Schematic Design Workflow
1. Open Library Manager
    1. Tools → Library Manager
2. Create new library
    1. File → New → Library
    2. name library and click **OK**
    3. Attach to an existing technology library → **OK**
    4. gpdk045 → **OK**
4. Create new cell
    1. New → Cell View
    2. File → Cell: INV/NAND/{YOUR_COMPONENT_HERE}
    3. click the cell
5. Create an instance
    1. Add Instance → Create → Instance
    2. **gpdk045 → pmos/nmos**
    3. add wires using **w**
    4. add **Vdd** and **gnd** using **analogLib → vdd** or **gnd**
6. Launch and configure ADE L
    1. Launch → ADE L
    2. Setup → Stimuli
        1. gnd/gnd: Enabled; Function: dc; DC voltage: 0
        2. Vdd/gnd: Enabled; Function: dc; DC voltage: 1
        3. In/gnd: Enabled; Function: pulse;
            1. Voltage 1: 0
            2. Voltage 2: 1
            3. Period: 10n
            4. Delaytime: 2.5n
            5. Rise time: 10p
            6. Fall time: 10p
            7. Pulse width: 5n
    3. Analyses → Choose
        1. Analysis: trans; Stop Time: 10n; Enabled
    4. Ouputs → To Be Plotted → Select On Design
        1. In, Out
    5. Press **run** button
7. Analyze the waveforms
    1. Split waves (top right)
    2. Right click, drag to some part to zoom in
    3. Click on 1st curve, press **a**, press **q**, 500mv
    4. Click on 2nd curve, press **b**, press **q**, 500mv
    5. Should get difference between 2 points
### Layout Design Workflow
1. Open Library Manager
    1. Tools → Library Manager
2. Create new library
    1. File → New → Library
    2. name library and click **OK**
    3. **Attach to an existing technology library → OK**
    4. **gpdk045 → OK**
3. Create new cell
    1. New → Cell View
    2. File → Cell: INV/NAND/{YOUR_COMPONENT_HERE}
        - View: layout; Type: layout
    3. click the cell
4. Create an instance
    1. Add Instance → Create → Instance
    2. **gsclib045_tech → celltempl**
        1. usually keep cell height, change cell width
    3. **gpdk045 → pmos/nmos**
5. Create wires
    1. Choose **Poly** material → **r** for Rectangle
    2. Connect pmos gates to nmos
6. Create connections
    1. Choose **metal1** material → **r**
    2. Connect pmos drain to nmos source (doesn’t matter which)
    3. Connect pmos source to Vdd
    4. Connect nmos drain to gnd
7. Add the actual Vdd and gnd pins
    1. Create → Pin (Vdd, gnd)
    2. Change height to 0.05
    3. Type InputOutput
8. Add In and Out pins
    1. Create → **Via**
    2. Via Definition: M1_PO
    3. Create → Pin (In, Out)
    4. Remember to change type input/output
9. Save
10. Run DRC (Design Rule Check)
    1. PVS → Run DRC
    2. Run Data → Run Directory: DRC
    3. Rules → Technology: gpdk045_pvs
    4. Input → Convert Pin: Geometry + Text
    5. Submit
11. Run LVS (Layout vs Schematic)
    1. PVS → Run LVS
    2. Run Data → Run Directory: LVS
    3. Rules → Technology: gpdk045_pvs
    4. Input → Convert Pin: Geometry + Text
    5. Submit
12. Run Simulation
    1. Verify → Extract
    2. Rules File: `diva/divaEXT.rul`
    3. **Deselect** _**Rules Library**_
    4. OK
13. Verify Extracted Cell View
    1. Library Manager → demo → inv → **extracted**
    2. double click ⇒ run the simulation (same as running in schematic)