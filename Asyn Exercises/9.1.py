import numpy as np

if __name__ == "__main__":
    #A = np.array((3,3)).fill(np.random.randint(0,100))
    A = np.random.randint(0,100,(3,3))
    print(A)
    B = A
    B*= 0
    print(A)
    print(B)
    C = np.copy(A)
    C+=1
    print(A)
    print(B)
    print(C)