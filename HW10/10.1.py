import numpy as np
import pandas as pd


def cramer(mat, constants):
    #Determinant of the main matrix
    detMat = np.linalg.det(mat)
    # Determinant of the first substitution
    D1 = np.linalg.det(np.array([constants, mat[:,1], mat[:,2]]))
    # Determinant of the second substitution
    D2 = np.linalg.det(np.array([mat[:,0],constants, mat[:,2]]))
    # Determinant of the third substitution
    D3 = np.linalg.det(np.array([mat[:,0],mat[:,1],constants]))

    #Results of dividing the determinants of the substitutions by the determinant of the main matrix
    res = [D1/detMat, D2/detMat, D3/detMat]
    return res

if __name__ == "__main__":
    A = np.array([[5,-14,-3],[1,2,2],[-7,4,5]])
    C = np.array([-39,-2,-29])
    
    res = cramer(A,C)
    print(res)