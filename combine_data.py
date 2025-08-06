import csv

data = {}

with open('dd_fin.csv', encoding='utf-8') as fh:
    next(fh)
    for line in fh:
        line = line.rstrip()
        entries = line.split(',')
        data[entries[0]] = {'conf': entries[1]}

with open('pep_length.csv', encoding='utf-8') as fh:
    for line in fh:
        line = line.rstrip()
        entries = line.split(',')
        data[entries[0]]['len'] = entries[1]
        
with open('dd_stats2.csv', encoding='utf-8') as fh:
    next(fh)
    for line in fh:
        line = line.rstrip()
        entries = line.split(',')
        data[entries[0]]['ave'] = entries[1]
        data[entries[0]]['sd'] = entries[2]

print("Peptide,Avg dist,Stddev,Length,Confidence")
for peptide in data:
    print(f"{peptide},{data[peptide]['ave']},{data[peptide]['sd']},{data[peptide]['len']},{data[peptide]['conf']}")
