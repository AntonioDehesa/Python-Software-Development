import numpy as np

n = 10000

if __name__ == "__main__":
    numbers = np.random.rand(n,1)
    print(numbers)
    # We get the mean
    mean = np.mean(numbers)

    # We get the standard deviation
    stdev = np.std(numbers)

    print("Mean of the distribution: {}. \nStandard deviation : {}".format(mean, stdev))