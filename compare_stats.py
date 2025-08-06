import csv

with open('dd_stats2.csv','r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 

    print("Peptide,Avg dist,Stddev,Length,Confidence")  
    for row in plots:
        print(row)
        if (row[3]!='Length') & (row[1]!="Average"):
            if (float(row[3]) > float(row[1])):
                print(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]}")


