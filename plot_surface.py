import matplotlib.pyplot as plt
import csv

x = [] 
y = []


with open('dd_test2.csv','r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
      
    for row in plots: 
        x.append(row[6]) 
        y.append(row[7])
        
plt.plot(x, y)
plt.xlabel('Confidence')
plt.ylabel('Sample')
plt.title('Sample vs Confidence')
plt.show()