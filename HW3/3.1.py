from code import interact
import csv
import math

def populationExponentialGrowth(a,d_t,x0,t, maxTime):
    res = []
    currentTime = t
    currentValue = 0
    with open("exponential.csv", "w", newline="") as my_file:
        headers = ["Value","t"]
        writer = csv.DictWriter(my_file, fieldnames=headers, dialect="excel")
        writer.writeheader()
        while currentTime < maxTime:
            writer.writerow({"t":currentTime, "Value": currentValue})
            currentValue = (math.e)**(a*currentTime)
            currentTime+=d_t
            currentTime = round(currentTime,1)
        writer.writerow({"t":currentTime, "Value": currentValue})
    
if __name__ == "__main__":
    a = 5
    d_t = 0.1
    x0 = 1000
    t = 0
    populationExponentialGrowth(a,d_t,x0,t,2)