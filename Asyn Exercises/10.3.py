import numpy as np
import pandas as pd
import seaborn as sn
from os import PathLike

if __name__ == "__main__":
    iris = sn.load_dataset("iris")
    print(type(iris))
    iris["prod_pet_len_wid"] = iris["petal_length"]*iris["petal_width"]
    iris["prod_sep_len_wid"] = iris["sepal_length"]*iris["sepal_width"]
    print(iris.info())
    print(iris.describe().iloc[-5:,]) # we print the 5-number summary, using the describe method.
    iris.to_csv("./iris.csv")
