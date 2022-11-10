import random as rd
import statistics as st

"""
Draw 1000 random numbers (with replacement) from each of the following distributions and display their means and standard deviations: integer,
uniform, normal. You may choose parameters.
Hint: import random, array, statistics. 
"""
n = 1000
min = 0
max = 100000 #100,000

#For the total number of elements, I decided to get 10 times the elements to draw, to get a decent size population
def normal_distribution(elements):
    #For the random package, gauss = normal distribution. In this case, as we can select the parameters, I choose the ones in the example of the
    # documentation for the package: mu = 15.0 and sigma = 3.5
    return [rd.gauss(15.0,3.5) for _ in range(0,elements*10)]

def uniform_distribution(elements, min, max):
    return [rd.uniform(min,max) for _ in range(0,elements*10)]

def integer_distribution(elements, min, max):
    return [rd.randrange(min, max) for _ in range(0,elements*10)] # Returns a random integer from min to max, {elements} times. 

if __name__ == "__main__":
    int_dist = integer_distribution(n, min, max)
    uni_dist = uniform_distribution(n, min, max)
    nor_dist = normal_distribution(n)

    # We get the means
    mean_int_dist = st.mean(int_dist) # Returns the mean (arithmetic mean) for int_dist

    mean_uni_dist = st.mean(uni_dist)

    mean_nor_dist = st.mean(nor_dist)

    # We get the standard deviations (for samples).
    stdev_int_dist = st.stdev(int_dist)
    stdev_uni_dist = st.stdev(uni_dist)
    stdev_nor_dist = st.stdev(nor_dist)

    print("Mean of the integer distribution: {}. \nStandard deviation for the integer distribution: {}".format(mean_int_dist, stdev_int_dist))
    print("Mean of the uniform distribution: {}. \nStandard deviation for the uniform distribution: {}".format(mean_uni_dist,stdev_uni_dist))
    print("Mean of the normal distribution: {}. \nStandard deviation for the normal distribution: {}".format(mean_nor_dist, stdev_nor_dist))