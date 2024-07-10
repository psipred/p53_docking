import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import csv

x = [] 
y = []
z = []

fig, ax = plt.subplots(subplot_kw={"projection": "3d"}) 
with open('dd_test2.csv','r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
      
    for row in plots: 
        x.append(row[6]) 
        y.append(row[7])
        z.append(row[8])
        
 
plt.xlabel('Confidence')
plt.ylabel('Sample')

surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False) 
plt.title('3D plot')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()