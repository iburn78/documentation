# CSV: Comma-Separated-Values (TSV: Tab SV, SSV: Space SV)
'''
Rules
- One data for a line 
- First line can be used as a header
- use "", if there is escape char or , or " itself (escape for " is "")

Notes
- XML is no longer used
- Easy to understand: XML > JSON > CSV 
- Size: CSV > JSON > XML

'''
csv = """\
p, x, s, n, t, p
e, x, s, y, t, a
e, b, s, w, t, l\
"""

splitted = csv.split("\n")
for item in splitted:
    list_mushroom = item.split(",")
    print(list_mushroom)



# Note on using CSV from EXCEL or Internet
'''
- When exporting CSV using EXCEL in Windows, "euc-kr" encoding is automatically applied (otherwise indicated as "utf-8")
- In order to read CSV file encoded with "euc-kr", use "codes" module 
'''

import csv, codecs

filename = "test.csv"
file = codecs.open(filename, "r", "euc-kr")

reader = csv.reader(file, delimiter=",") # if quotes are used in each data, use quotechar='"' 
for cells in reader:
    print(cells[1], cells[2])


