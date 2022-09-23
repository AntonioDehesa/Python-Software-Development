from code import interact
import csv

balanceBOY = float(input("How much do you want to invest?"))
interest_rate = 0.05
years = int(input("For how many years do you want to invvest?"))

balanceEOY = 0

with open("tracker.csv", "w", newline="") as my_file:
    headers = ["year","BOY Balance", "Interest", "EOY Balance"]

    writer = csv.DictWriter(my_file, fieldnames=headers, dialect="excel")
    writer.writeheader()
    
    for i in range(years):
        interest = balanceBOY*interest_rate
        balanceEOY = balanceBOY+interest
        writer.writerow({"year":i+1, "BOY Balance": balanceBOY, "Interest": interest, "EOY Balance": balanceEOY})
        balanceBOY = balanceEOY