import numpy as np
import pandas as pd
import seaborn as sn

if __name__ == "__main__":
    url = "https://raw.github.com/mattdelhey/kaggle-titanic/master/Data/train.csv"
    titanic = pd.read_csv(url)
    titanic["age"].fillna(value=titanic["age"].mean(), inplace=True) # Replace missing values with the mean, for column age
    titanic = titanic.dropna(axis=1) # Drop columns with missing values

    print(titanic)
