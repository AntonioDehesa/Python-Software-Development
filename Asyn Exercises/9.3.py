import numpy as np

if __name__ == "__main__":
    #A = np.array((3,3)).fill(np.random.randint(0,100))
    A = np.random.randint(0,100,(3,3))
    B = np.array([1,2,3])
    C = A.dot(B)
    print(C.shape)
    D = np.random.exponential(scale=1/15,size=1000)
    print("Mean: {}".format(D.mean()))
    print("Standard deviation: {}".format(D.std()))
    print(D.min())
    print("Q1: {}\nQ3: {}", np.percentile(D,[25,75]))
    print(D.max())