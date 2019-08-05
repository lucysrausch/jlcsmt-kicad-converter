#!/usr/bin/env python3
# coding=utf8
import sys
import csv
from collections import OrderedDict
from difflib import SequenceMatcher

package_remap = {
    "C_0603_1608Metric": "0603_C",
    "R_0603_1608Metric": "0603_R",

    "C_0805_2012Metric": "0805_C",
    "R_0805_2012Metric": "0805_R",

    "LED_0603_1608Metric": "LED_0603",

    "SOIC-8_3.9x4.9mm_P1.27mm": "SOIC-8_150mil",
    "LQFP-64_10x10mm_P0.5mm": "LQFP-64_10x10x05P",
    "Crystal_SMD_SeikoEpson_FA238V-4Pin_3.2x2.5mm": "SMD-3225_4P",
    "SOT-23-6-small": "SOT-23-6"
 }

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

in_file = open(sys.argv[1], 'r')
out_file = open(sys.argv[2], 'w')

match_lib = 0
if (len(sys.argv) > 3):
    match_lib = 1
    print("Using LCSC part lib")

reader = csv.DictReader(in_file, delimiter=';')

ordered_fieldnames = OrderedDict([('Comment',None),('Designator',None),('Footprint',None),('LCSC Part #',None),('LCSC Part Type',None)])
writer = csv.DictWriter(out_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC, fieldnames=ordered_fieldnames)
writer.writeheader()


#{'Comment': '1M', 'Layer': 'TopLayer', 'Description': 'Resistor 1', 'Footprint Description': 'Chip Resistor, Body 1.6x0.8mm, IPC Medium Density', 'Designator': 'R33', 'ComponentKind': 'Standard', 'Ref-X(mm)': '291.604', 'Height(mm)': '0.600', 'Ref-Y(mm)': '79.777', 'Variation': 'Fitted', 'Pad-X(mm)': '291.604', 'Footprint': 'R-0603-M', 'Center-Y(mm)': '79.777', 'Pad-Y(mm)': '80.577', 'Rotation': '270', 'Center-X(mm)': '291.604'}
for row in reader:
    name, value, package, num = [row['Designator'], row['Designation'], row['Package'], row['Quantity']]
    package = package_remap.get(package, package)

    print("########    Part " + str(value) + " in " + str(package) + "   #########")
    lcsc_partnr = None
    lcsc_parttype = None
    if (match_lib == 1):
        partnrDic = {}
        valueDir = {}
        partlib = csv.DictReader(open(sys.argv[3], 'r'), delimiter=';')

        for part in partlib:
            lib_partnr, lib_value, lib_package, lib_parttype, lib_cat  = [part['Part #'], part['Comment'], part['Package'], part['Type'], part['Category']]
            search_coeff = 0
            if (similar(package, lib_package) > 0.75):
                if value in lib_value.lower() or lib_value.lower() in value:
                    search_coeff += 1.0 # prefer exactly matching parts
                if "Basic" in lib_parttype:
                    search_coeff += 0.2 # prefer "Basic" components

                if "_R" in package:# or ("_C" in package and "Capacitor" in lib_cat):
                    if "Resistor" in lib_cat: # improve results for resistors
                        partnrDic.update({str(lib_partnr) : (similar(value, lib_value) + search_coeff)})
                        valueDir.update({str(lib_partnr) : (str(lib_value) + str(", ") + str(lib_parttype))})
                else:
                    partnrDic.update({str(lib_partnr) : (similar(value, lib_value) + search_coeff)})
                    valueDir.update({str(lib_partnr) : (str(lib_value) + str(", ") + str(lib_parttype))})

        print("Most likely:")
        found = len(partnrDic)
        if (found > 0):
            for i in range(min(found, 3)):
                maximum = max(partnrDic, key=partnrDic.get)

                if (partnrDic[maximum] > 2.0):
                    print(valueDir[maximum] + ", " + str(int((partnrDic[maximum] - 2.0) * 100)) + "%:")
                elif (partnrDic[maximum] > 1.0 and partnrDic[maximum] < 2.0):
                    print(valueDir[maximum] + ", " + str(int((partnrDic[maximum] - 1.0) * 100)) + "%:")
                else:
                    print(valueDir[maximum] + ", " + str(int(partnrDic[maximum] * 100)) + "%:")
                print(str(maximum))
                del valueDir[maximum]
                del partnrDic[maximum]
        else:
            print("Nothing found :(")

    writer.writerow({'Comment': value, 'Designator': name, 'Footprint': package, 'LCSC Part #': lcsc_partnr, 'LCSC Part Type': lcsc_parttype})

in_file.close()
out_file.close()

sys.exit(1)
