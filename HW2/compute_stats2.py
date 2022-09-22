from asyncore import read
from statistics import mean, median
import sys
import csv

def read_Data(data : str, isFile, column : int):
    values = []
    if isFile:
        with open(data, 'r') as my_file:
            heading = next(my_file)#We get the heading and skip the first line
            reader = csv.reader(my_file, delimiter=" ")
            for row in reader:#We add each number to the previous lists
                pass
    else:
        reader = csv.reader(data, delimiter=" ", skipinitialspace=True)
        for row in reader:
            values.append(float(row[column-1]))
    return values

def compute_stats(values: list[float] = []):
    if not values:
        return None
    o_min = min(values)
    o_max = max(values)
    o_avg = mean(values)
    o_median = median(values)
    return o_min, o_max, o_avg, o_median

def main():
    col = int(sys.argv[1])
    #numbers = [float(x) for x in sys.stdin if float(x) > -9999.0] #With this, we make sure to delete the 'missing data' values
    numbers = sys.stdin
    if len(sys.argv) > 2:
        numbers = read_Data(sys.argv[2], True, col)
    else:
        numbers = read_Data(numbers, False, col)
    numbers.sort()
    res = compute_stats(numbers)
    if res == None:
        print("Result could not be computed with the provided values")
    else:
        print("min: {}, max: {}, average: {}, median: {}".format(*compute_stats(numbers)))

if __name__ == "__main__":
    main()