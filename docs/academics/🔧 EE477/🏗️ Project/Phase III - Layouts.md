Notion does not export to PDF very elegantly, for a better viewing experience visit the link below:
[https://www.notion.so/Phase-III-Layouts-5f5c29b379c840fab5893386e821cb11?pvs=4](https://www.notion.so/Phase-III-Layouts-5f5c29b379c840fab5893386e821cb11?pvs=4)
This group has the following 3 members:
- Kylie Morales
- Scott Susanto
- Felix Chen
## Front Page
- Provide a table with the performance metrics number. Create a table with 4 rows (area, delay, power, PAD) and 2 columns (schematic, extracted). Write down the values based on your simulation results. (Note: there will be no area number for the schematic column).

|       | Schematic | Extracted                    |
| ----- | --------- | ---------------------------- |
| Area  | -         | 10,585.45$nm^2$              |
| Delay | 381.95ps  | 367.31ps                     |
| Power | -         | $192.1W * 10^{-6}$           |
| PAD   | -         | $7.704 * 10^{-10}W\mu m^2ps$ |

- Mention the total number of metal layers you have used for the complete system layout. 
	Total of 6 metal layers used.
- Create another table with your teammates' names and the work distribution throughout the project (consider all project phases).
	
|       | Phase I                  | Phase II                    | Phase III                                               |
| ----- | ------------------------ | --------------------------- | ------------------------------------------------------- |
| Kylie | Part 3: DIVIDER          | Part 2: Minimum Time Period | Arbiter Layout                                          |
| Felix | -                        | Part 1: Arbiter             | FA Layout + MULT Layout, PAD Reports, Power measurement |
| Scott | Part 1: FA, Part 2: MULT | Part 2: DFF                 | DIVIDER Layout + PROJ Layout                            |

## Part 1: Layouts
### Multiplier
**HA**
- LVS
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/ec45ddd9-ec79-480e-8bfe-1724c2a00a5b/Untitled.png)
- DRC
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/f3d05439-c4b0-4d6f-b8fb-d61f58a8e286/Untitled.png)

**FA**
- LVS
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/70c40021-5a88-4ec2-965b-2c028a987b19/Untitled.png)
- DRC
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/c8dddb51-8567-420b-816e-d8050ba88a48/Untitled.png)
**AND**
- LVS
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/18f6829b-ea3e-4980-9e01-b1af133ee7f2/Untitled.png)
- DRC
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/eb651427-b274-4f75-b639-e7c4147bef88/Untitled.png)
**MULT**
- LVS
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/08174d5b-9e2b-4fe0-b969-fa8818a26ec3/Untitled.png)
- DRC
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/c4491af3-295e-4b7a-8a5d-36a670587e8a/Untitled.png)
- Functional Verification
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/6d53af0a-bb8d-4945-b6d0-e2a8241e1fbe/Untitled.png)
### Divider
**HS**
- LVS
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/a7a9e025-c1c5-4ff1-86ad-5b9400d143d8/Untitled.png)
- DRC
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/cf9ff4c6-0ee7-4511-9c38-e6acdc7a3f1a/Untitled.png)
**FS**
- LVS
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/1760126f-521f-47bb-b6b2-eb0816e123d0/Untitled.png)
- DRC
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/03cc7e48-cc05-4aef-a864-3025faaf5f5b/Untitled.png)
**MUX**
- LVS
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/24a46a77-1c9e-4b9d-bb2d-f949e2cd2013/Untitled.png)
- DRC
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/a44d8357-3e2b-4e3d-b45e-bd31a83ccf6a/Untitled.png)
**HS_MUX**
- LVS
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/c6af0d9c-a45a-4d94-8c3c-57dfd6701061/Untitled.png)
- DRC
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/6673bad7-c0f0-4ef6-bc15-17b0c1d947a9/Untitled.png)
**FS_MUX**
- LVS
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/e98ab96b-852c-427a-aaae-816c439107ed/Untitled.png)
- DRC
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/add73d7f-b36f-4de2-ab68-a7e27b90b9d5/Untitled.png)
**DIVIDER**
- LVS
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/48ecd4e7-3d8a-40ab-8520-73d1e2ff11c6/Untitled.png)
- DRC
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/a09eb2e3-f52e-4ef7-a86b-39442b4812c2/Untitled.png)
- Functional Verification
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/e7b6af15-e9f6-45a9-a4ec-92f0d8e201f9/Untitled.png)
    or, an easier way to verify is perceiving it through unsigned decimal:
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/99876c7c-dc37-4251-90b8-15a40a685437/Untitled.png)
### Arbiter
- LVS & DRC
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/96a43762-8c0f-4c0b-b0ab-8c5707f6fa50/Untitled.png)
**NAND3X4**
- LVS & DRC
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/139451ce-e1d5-4b41-baf6-5ea76150f45d/Untitled.png)
**AND3X4**
- LVS & DRC
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/a8b32e52-d0a8-4bf0-9718-b19e7e96c03a/Untitled.png)
**DFF**
- LVS & DRC
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/d8284165-7a42-4949-9f70-38db3c4207cf/Untitled.png)
**DFF_4BIT**
- LVS & DRC
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/47b9f5b4-4d2a-40e3-9b90-879bea90ef85/Untitled.png)
**DFF_8BIT**
- LVS & DRC
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/0cdb6605-9ff0-4b52-b4bb-eb3a2976adee/Untitled.png)
**MUX_8BIT**
- LVS
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/2f254423-19e9-4b19-96f5-6495c36a13b1/Untitled.png)
- DRC
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/5af8c35b-c1c6-49de-a1f4-b17ae26e34d2/Untitled.png)
    

**Buffer**

- LVS
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/4601d240-13ea-47ff-8379-d6d64c20bfd1/Untitled.png)
- DRC
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/2009ec01-157d-4e5f-bd68-09f5abfb59cd/Untitled.png)
### Complete Layout
- Schematic
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/cd53de37-661c-4022-8d78-448d3fa12219/Untitled.png)
- Schematic Functional Verification
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/02b7df90-1f62-431b-ab5c-a1b0b97c961f/Untitled.png)
- LVS
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/b96ade11-e866-484c-a4ba-941d061b6ac3/Untitled.png)
- DRC
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/6247a8d4-3f93-4785-8210-e90cb6fe34b5/Untitled.png)
- Extracted Functional Verification
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/abe28638-0325-4cd6-a140-db4efcc6cac7/Untitled.png)
## Part 2: Performance
### Area
- Layout
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/520a9746-ecf9-4dc6-8f67-f6022ee80c99/Untitled.png)
    $Area = 131.48nm * 80.51nm = 10585.4548nm^2$
### Delay
- Schematic
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/a62567ff-c341-477b-92f9-ba71382ce96f/Untitled.png)
- Layout
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/9c1d8a75-c7da-49ae-80ef-6c96e6b09121/Untitled.png)
### Power
Graph
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/5981813d-797d-411e-bf12-3c2ff4899fbc/Untitled.png)
Average current calculation:
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3696531b-04a1-4549-809f-e2f49abf75fe/eec0ca49-d60b-4ed9-9808-a088c87dabc4/Untitled.png)
The average power = $192.1A * 10^{-6} * 1V = 192.1W * 10^{-6}$
### PAD
- Power = $192.1\times10^{-6}W$
- Area = $0.0105\mu m^2$
- Delay = $381.95ps$
- **PAD =** $7.704\times10^{-10}W\mu m^2ps$
## Optimizations
- none made
## Final Notes
- thank you for an amazing semester 👍
