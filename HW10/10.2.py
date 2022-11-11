import pandas as pd


if __name__ == "__main__":
    columns = ["Math", "Science", "English", "History"]
    row1 = pd.Series([80,89,93,66,84,85,74,64])
    row2 = pd.Series([94,76,88,78,88,92,60,85])
    row3 = pd.Series([83,76,93,96,77,85,92,60])
    row4 = pd.Series([96,66,76,85,78,88,69,99])
    grades = pd.DataFrame(list(zip(row1,row2,row3,row4)), columns=columns)
    print("Student´s grades\n")
    print(grades)
    print() # print empty line, just to format the data a little better
    print("Mean\n")
    print(grades.mean().to_string() + "\n") # we stringify the mean series, just to not print the type
    print("Standard deviation\n")
    print(grades.std().to_string() + "\n") # same as the mean
    print(grades.describe().iloc[-5:,]) # we print the 5-number summary, using the describe method.