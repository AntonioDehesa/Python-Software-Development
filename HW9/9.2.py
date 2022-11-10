import numpy as np

"""
Draw 1000 random numbers (with replacement) from each of the following distributions and display their means and standard deviations: integer,
uniform, normal. You may choose parameters.
"""
n = 1000
min = 0
max = 100000 #100,000

if __name__ == "__main__":
    int_dist = np.random.randint(low=max,size=n)
    uni_dist = np.random.uniform(min,max,n)
    nor_dist = np.random.normal(15.0,3.5, n)

    # We get the means
    mean_int_dist = np.mean(int_dist)#st.mean(int_dist)

    mean_uni_dist = np.mean(uni_dist)#st.mean(uni_dist)

    mean_nor_dist = np.mean(nor_dist)#st.mean(nor_dist)

    # We get the standard deviations (for samples).
    stdev_int_dist = np.std(int_dist)#st.stdev(int_dist)
    stdev_uni_dist = np.std(uni_dist)#st.stdev(uni_dist)
    stdev_nor_dist = np.std(nor_dist)#st.stdev(nor_dist)

    print("Mean of the integer distribution: {}. \nStandard deviation for the integer distribution: {}".format(mean_int_dist, stdev_int_dist))
    print("Mean of the uniform distribution: {}. \nStandard deviation for the uniform distribution: {}".format(mean_uni_dist,stdev_uni_dist))
    print("Mean of the normal distribution: {}. \nStandard deviation for the normal distribution: {}".format(mean_nor_dist, stdev_nor_dist))