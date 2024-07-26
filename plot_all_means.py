import matplotlib.pyplot as plt
import csv
import numpy as np

x = []
y = []
with open('bad_pep.csv','r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        if (row[1]!='Avg dist') & (row[0]!="Peptide"):
            x.append(row[1])
            y.append(row[0])

ax = plt.subplot()
ax.hist(x, bins= 150, width = 2.7)
plt.ylabel('Count')
plt.xlabel('Mean distance from rank1')
plt.title('Mean plot for bad peptides')
#ax.set_xticks(np.arange(0, 1000.1, 100))
plt.show()
#print(x)
