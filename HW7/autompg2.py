import errno
from os import path,strerror
import csv
from collections import namedtuple
import logging
import requests
import argparse
from sys import argv

######  Logging configuration  #######
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

#file Handler
fh = logging.FileHandler("autompg2.log")
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

# stream handler aka console
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
logger.addHandler(sh)

Record = namedtuple("Record",["MPG","cylinders","displacement","horsepower","weight","acceleration","Year","origin","carName"])
class AutoMPG():
    def __init__(self,make: str = "", model: str = "", year: int = 0, mpg: float = 0.0) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.mpg = mpg
        logging.info("New AutoMPG object created")

    def __repr__(self) -> str:
        #logging.info("Repr of: {}".format(str(self)))
        return "AutoMPG({})".format(str(self))

    def __str__(self) -> str:
        return "make= \"{}\", model= \"{}\", year= {}, mpg= {}".format(self.make,self.model,self.year,self.mpg)
    
    def __eq__(self, other: object):
        if isinstance(other, self.__class__):
            return True if (self.make, self.model, self.year, self.mpg) == (other.make, other.model, other.year, other.mpg) else False
        logging.debug("{} was being compared to a non-AutoMPG object".format(str(self)))
        return "Not yet implemented"
    
    def __lt__(self, other:object):
        if isinstance(other, self.__class__):
            a = (self.make, self.model, self.year, self.mpg)
            b = (other.make, other.model, other.year, other.mpg)
            return a < b
        else:
            logging.debug("{} was being compared to a non-AutoMPG object".format(str(self)))
            return "Not yet implemented"
    def __ge__(self, other:object):# Added this method to make the testing stage easier
        return self == other or not self < other

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
            logging.debug("End of the iteration")
            raise StopIteration
        res = self.data[self.__iter]
        self.__iter += 1
        return res
    def __load__data(self):
        if not path.exists("auto-mpg.clean.txt"):
            logging.debug("auto-mpg.clean.txt file was not found")
            if path.exists("auto-mpg.data.txt"):
                self.__clean_data()
            else:
                logging.debug("auto-mpg.data.txt file was not found")
                self._get_data()
        if path.exists("auto-mpg.clean.txt"):
            with open("auto-mpg.clean.txt", 'r') as my_file:
                #heading = next(my_file)#We get the heading and skip the first line
                reader = csv.reader(my_file, delimiter=" ", skipinitialspace=True)
                for row in reader:#We add each number to the previous lists
                    tempRecord = Record(*list(row))
                    tempAutoMPG = AutoMPG(str(tempRecord[8]).split()[0],
                    " ".join(str(tempRecord[8]).split()[1:]), int(tempRecord[6])+1900, float(tempRecord[0]))
                    self.data.append(tempAutoMPG)
                logging.info("Completed the loading data step")
        else:
            logging.error("Data was not succesfully loaded. Closing the application")
            raise FileNotFoundError(errno.ENOENT, strerror(errno.ENOENT), "auto-mpg.clean.txt")

    def __clean_data(self):
        clean = open("auto-mpg.clean.txt","w")
        myData = open("auto-mpg.data.txt", "r")
        for line in myData:
            clean.write(line.expandtabs())
        clean.close()
        myData.close()
        logging.info("Completed the cleaning data step")
    
    def sort_by_default(self):
        self.data.sort()
        logging.info("Sorted the data list by default")

    def sort_by_year(self):
        self.data.sort(key= lambda autompg: autompg.year)
        logging.info("Sorted the data list by year")

    def sort_by_mpg(self):
        self.data.sort(key= lambda autompg: autompg.mpg)
        logging.info("Sorted the data list by MPG")

    def _get_data(self):
        url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
        response = requests.get(url)
        if response.status_code == 200:
            clean = open("auto-mpg.data.txt","w")
            clean.write(response.text)
            clean.close()
            logging.info("Data succesfully retrieved from URL: {}".format(url))
            self.__clean_data()
        else:
            logging.error("The data was not succesfully retrieved from the url: {}. \nStatus code: {}".format(url,response.status_code))
    
def parser(args):
    #######     Argparse configuration     #######
    parser = argparse.ArgumentParser(description="""Arranges the data by car model, manufacturer, year, and mpg. 
    Then, it displays it, either by the order in which they came in first, by year, or by mpg.""")

    parser.add_argument("print", metavar="<print>", type=str, help="This command will print the elements of the AutoMPGData collection.")
    parser.add_argument("-s", "--sort order", choices=["year", "mpg", "default"],dest="sortOrder", action="store", help="Decides the sorting order used before printing the elements.")
    return parser.parse_args(args)

if __name__ == "__main__":
    args = parser(argv[1:])
    a = AutoMPGData()
    if args.sortOrder == "" or args.sortOrder == None:
        a.sort_by_default()
    elif args.sortOrder == "year":
        a.sort_by_year()
    else:
        a.sort_by_mpg()
    for x in a:
        print(repr(x))