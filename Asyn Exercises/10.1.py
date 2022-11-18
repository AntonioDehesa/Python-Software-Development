import numpy as np
import pandas as pd

if __name__ == "__main__":
    jersey = [1,2,3,4,5,6,7,8,9,10]
    names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    list1 = np.array(jersey)
    labels = np.array(names)
    res = pd.Series(data=list1, index=labels)
    print(res)
    df = pd.DataFrame(res)
    df["Col3"] = np.random.rand(len(jersey))
    df["Col4"] = np.random.rand(len(jersey))
    print(df)