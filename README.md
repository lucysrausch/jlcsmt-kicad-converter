# jlcsmt-kicad-converter
Converts kicad .csv BOM files to JLCSMT compatible BOM format. 

This script was created as a fast way of converting kicad BOMs to a BOM format as provided as an example on https://jlcpcb.com/smt-assembly
Appearantly it is required for the footprint description to match the description in the JLCSMT parts library.
For this, you can add parts you use to a replacement list at the beginning of the script.

Usage:
`python3 kicad2lcscBOM.py input.csv output.csv`

Optional:
JLC provides a parts library with available parts for SMT service: https://jlcpcb.com/video/jlcsmt_parts_library.xls
If you want to get suggestions for possible part numbers, use the script the following way:

`python3 kicad2lcscBOM.py input.csv output.csv jlcsmt_parts_library.csv`

The search was optimized for my needs. Eg Basic parts are preffered as there are no additional costs.
This is super hacking and might not work for your needs, but for me it is a nice way of quickly matching the recommended part numbers.

Sample output:

```
niklas@niklas-precision:~/pnptools$ python3 kicad2lcscBOM.py pcb_module.csv lcsc_bom.csv jlcsmt_parts_library.csv 
Using LCSC part lib
########    Part 1k in 0603_R   #########
Most likely:
1KΩ (102) ±5%, Basic Part, 31%:
C20197
1KΩ (1001) ±1%, Basic Part, 31%:
C21190
91KΩ (9102) ±1%, Basic Part, 30%:
C23265
########    Part MPCIE-Socket in mpcie-full-card-edit   #########
Most likely:
Nothing found :(
########    Part 1n in 0603_C   #########
Most likely:
1nF (102) ±10% 50V X7R, Basic Part, 35%:
C1588
1nH ±0.3nH, Extended Part, 30%:
C1027
1nH ±0.3nH, Extended Part, 30%:
C41902
########    Part 100n in 0603_C   #########
Most likely:
100nH ±5%, Extended Part, 57%:
C49329
100nH ±5%, Extended Part, 57%:
C74310
100nF (104) ±10% 50V X7R, Basic Part, 47%:
C14663
########    Part LED in LED_0603   #########
Most likely:
翠绿LED, Extended Part, 50%:
C205443
翠绿LED, Extended Part, 50%:
C118334
黄灯 贴片LED, Extended Part, 31%:
C84268
########    Part MAX485E in SOIC-8_150mil   #########
Most likely:
MAX3485ESA, Extended Part, 82%:
C18148
MAX485ESA+T, Extended Part, 77%:
C19738
MAX3485EESA, Extended Part, 77%:
C9943
########    Part 120 in 0603_R   #########
Most likely:
120Ω (1200) ±1%, Basic Part, 50%:
C22787
12KΩ (1202) ±1%, Basic Part, 50%:
C22790
1.2MΩ (1204) ±1%, Basic Part, 48%:
C22766
########    Part 220u in L_Bourns-SRN4018   #########
Most likely:
Nothing found :(
########    Part 0R25 in 0805_R   #########
Most likely:
0Ω (0R0) ±1%, Basic Part, 42%:
C17477
3MΩ (305) ±5%, Basic Part, 41%:
C26117
0.2Ω (0R2) ±5%, Extended Part, 40%:
C247066
########    Part MIC5504-3.3YM5 in SOT-23-5   #########
Most likely:
MIC5504-3.3YM5-TR, Extended Part, 90%:
C88419
MIC5205-3.3YM5, Extended Part, 85%:
C37970
MIC5219-3.3YM5, Extended Part, 78%:
C29613
########    Part 10u in 0805_C   #########
Most likely:
10uH ±10%, Basic Part, 66%:
C1046
10uH±5%, Extended Part, 54%:
C76742
10uF (106) ±10% 25V X5R, Basic Part, 42%:
C15850
```
