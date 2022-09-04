from statistics import mean, median
import sys

numbers = [float(x) for x in sys.stdin if float(x) > -9999.0] #With this, we make sure to delete the 'missing data' values
print("min: {}, max: {}, median: {}, average: {}".format(numbers[0],
                                                        numbers[-1], 
                                                        median(numbers),
                                                        mean(numbers)))
# As the list is sorted (and we know it is), for the min and max, 
# we can just print the first and last items in the list. 
# If they were not sorted, we would need to use min and max functions.