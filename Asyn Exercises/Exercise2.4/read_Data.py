import csv
from operator import index

# We create lists to store the numbers for each row
t = []
s = []
v = []
with open('data.csv', 'r') as my_file:
    heading = next(my_file)#We get the heading and skip the first line
    reader = csv.reader(my_file)
    for row in reader:#We add each number to the previous lists
        t.append(float(row[0]))
        s.append(float(row[1]))
        v.append(float(row[2]))
    maxRow = s.index(max(s))#We get the maximum number in the S numbers, and then we look 
                            #for its position in the list
    print("[{},{},{}]".format(t[maxRow], s[maxRow], v[maxRow]))# finally, we print 
                                                               #the numbers in that position