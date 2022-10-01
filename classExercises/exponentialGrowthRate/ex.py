from asyncore import read
#from code import interact
import csv

def read_file():
    data = []
    with open("population.csv", "r", newline="") as my_file:
        reader = csv.reader(my_file, delimiter=",")
        heading = next(my_file)#We get the heading and skip the first line
        data = [row for row in reader]
    print(data)

if __name__ == "__main__":
    read_file()