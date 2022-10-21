from os import path
import csv
from collections import namedtuple

Record = namedtuple("Record",["MPG","cylinders","displacement","horsepower","weight","acceleration","Year","origin","carName"])
class AutoMPG():
    def __init__(self,make: str = "", model: str = "", year: int = 0, mpg: float = 0.0) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.mpg = mpg

    def __repr__(self) -> str:
        return "AutoMPG({})".format(str(self))

    def __str__(self) -> str:
        return "make= \"{}\", model= \"{}\", year= {}, mpg= {}".format(self.make,self.model,self.year,self.mpg)
    
    def __eq__(self, other: object):
        if isinstance(other, self.__class__):
            if self.make == other.make and self.model == other.model and self.year == other.year and self.mpg == other.mpg:
                return True
            return False
        return "Not yet implemented"
    
    def __lt__(self, other:object):
        if isinstance(other, self.__class__):
            if self.make < other.make and not self.make > other.make:
                return True
            if self.model < other.model and not self.model > other.model:
                return True
            if self.year < other.year and not self.year > other.year:
                return True
            if self.mpg < other.mpg and not self.mpg > other.mpg:
                return True
            return False
        else:
            return "Not yet implemented"

    def __hash__(self) -> int:
        return hash(self.make) + hash(self.model) + hash(self.year) + hash(self.mpg)
        

class AutoMPGData():
    data = []
    def __init__(self) -> None:
        self.__load__data()

    def __iter__(self):
        self.__iter = 0
        return self
    
    def __next__(self):
        if self.__iter == len(self.data):
            raise StopIteration
        res = self.data[self.__iter]
        self.__iter += 1
        return res
    def __load__data(self):
        if not path.exists("auto-mpg.clean.txt"):
            self.__clean_data()
        with open("auto-mpg.clean.txt", 'r') as my_file:
            #heading = next(my_file)#We get the heading and skip the first line
            reader = csv.reader(my_file, delimiter=" ", skipinitialspace=True)
            for row in reader:#We add each number to the previous lists
                #print(list(row))
                tempRecord = Record(*list(row))
                tempAutoMPG = AutoMPG(str(tempRecord[8]).split()[0],
                " ".join(str(tempRecord[8]).split()[1:]), int(tempRecord[6])+1900, tempRecord[0])
                self.data.append(tempAutoMPG)

    def __clean_data(self):
        clean = open("auto-mpg.clean.txt","w")
        myData = open("auto-mpg.data.txt", "r")
        for line in myData:
            clean.write(line.expandtabs())
        clean.close()
        myData.close()
            

    pass


if __name__ == "__main__":
    a = AutoMPGData()
    for x in a:
        print(repr(x))