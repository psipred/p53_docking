import matplotlib.pyplot as plt 
import csv

x = [] 
y = [] 
  
with open('dd_test.csv','r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
      
    for row in plots: 
        x.append(row[3]) 
        y.append(row[1])
  
plt.plot(x, y) 
plt.xlabel('Confidence')
plt.ylabel('Sample') 
plt.title('Sample vs confidence')
plt.show() 