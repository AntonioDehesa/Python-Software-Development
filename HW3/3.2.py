from code import interact
import csv


def readFromCVS():
    data = []
    with open("elements.csv", "r", newline="") as my_file:
        reader = csv.reader(my_file, delimiter=",")
        heading = next(my_file)#We get the heading and skip the first line
        data = [row for row in reader]
    return data

def sortElements(elements):
    return elements.sort(reverse=True)


if __name__ == "__main__":
    data = readFromCVS()
    sortElements(data)
    print(data)