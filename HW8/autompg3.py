import errno
from os import path,strerror
import csv
from collections import namedtuple, defaultdict
import logging
import requests
import argparse
from sys import argv
from difflib import SequenceMatcher
import matplotlib.pyplot as plt
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
                    print(row)
                    tempRecord = Record(*list(row))
                    tempAutoMPG = AutoMPG(str(tempRecord[8]).split()[0],
                    " ".join(str(tempRecord[8]).split()[1:]), int(tempRecord[6])+1900, float(tempRecord[0]))
                    self.data.append(tempAutoMPG)
                logging.info("Completed the loading data step")
        else:
            logging.error("Data was not succesfully loaded. Closing the application")
            raise FileNotFoundError(errno.ENOENT, strerror(errno.ENOENT), "auto-mpg.clean.txt")

    def fix_typos(self, line):
        words = ["chevrolet", "mazda", "mercedes", "toyota", "volkswagen", 
                "ford", "bmw", "datsun", "hi", "pontiac", "amc", "buick", 
                "plymouth", "dodge", "opel", "fiat", "oldsmobile", "volvo",
                "renault", "honda", "subaru", "mercury", "cadillac",
                "triumph", "nissan", "peugeot", "audi", "chrysler"]
        # For this part, I used the sequencematcher library, to compare the words in the data
        # to a known pool of acceptable words. The threshold is high to avoid false positives
        # But it may cause issues, such as the very specific case of buick - opel. Both are 
        # car makers, so both have to be included in the acceptable word pool. But when we check
        # repeated car maker in the data, we have to delete one of them, which may cause issues. 
        threshold = 0.75
        line = line.replace('\"',"").split()
        #line = line.split()
        make = line[8]
        no_missing_model = True
        try:
            model = line[9]
        except IndexError:
            no_missing_model = False
        for word in words:
            if make == "vw":
                line[8] = "volkswagen"
                break
            if make == "chevy":
                line[8] = "chevrolet"
            # These two values had to be hard-coded, as the sequence matcher was not able to recognize them
            # with a threshold high enough to not cause issues. 
            similarityMake = SequenceMatcher(None, word, make).ratio()
            if similarityMake > threshold and similarityMake < 1.0:
                line[8] = "{}".format(word)
            if no_missing_model:
                similarityModel = SequenceMatcher(None, word, model).ratio()
                if similarityModel > threshold:
                    line.pop(9)
        
        line = "\t".join(line[0:8]) + "\t" + "\"" + " ".join(line[8:]) + "\""
        return line
    def __clean_data(self):
        print("Ratio")
        print(SequenceMatcher(None, "chevy", "chevrolet").ratio())
        clean = open("auto-mpg.clean.txt","w")
        myData = open("auto-mpg.data.txt", "r")
        for line in myData:
            temp = self.fix_typos(line)
            temp = temp.expandtabs()
            clean.write("{}\n".format(temp))
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
    
    def mpg_by_year(self):
        res = defaultdict(list)
        for tempAuto in self.data:
            res[tempAuto.year].append(tempAuto.mpg)
        for key in res:
            res[key] = sum(res[key])/len(res[key])
        return res

    def mpg_by_make(self):
        res = defaultdict(list)
        for tempAuto in self.data:
            res[tempAuto.make].append(tempAuto.mpg)
        for key in res:
            res[key] = sum(res[key])/len(res[key])
        return res

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

    parser.add_argument("command", metavar="<command>",nargs='?', 
                        type=str, help="Command to execute.")
    parser.add_argument("-s", "--sort order", choices=["year", "mpg", "default"], default="default",
                        dest="sortOrder", action="store", help="Decides the sorting order used before printing the elements.")
    parser.add_argument("-o", "--ofile", metavar="<outfile>", action="store", dest="outputFile",
                        help="Specify the output file. If none given, the output will be shown in sys.stdout")
    parser.add_argument('-p', '--plot', dest='do_plot', 
                        action='store_true', help='plot the data')
    return parser.parse_args(args)

def toPrint(printable, myFile, command):
    match command:
        case "print":
            if myFile:
                file = "" + myFile + ".csv"
                with open(file, "w+") as f:
                    headers = ["Make","Model", "Year", "MPG"]
                    writer = csv.DictWriter(f, fieldnames=headers, dialect="excel")
                    writer.writeheader()
                    for element in printable:
                        writer.writerow({"Make":element.make, "Model": element.model, 
                        "Year": element.year,"MPG": element.mpg})
            else:
                print(printable)
        case _:
            if myFile:
                file = "" + myFile + ".csv"
                with open(file, "w+") as f:
                    headers = [(command.split("_")[2]).capitalize(),"MPG"]
                    writer = csv.DictWriter(f, fieldnames=headers, dialect="excel")
                    writer.writeheader()
                    for key, value in printable:
                        writer.writerow({(command.split("_")[2]).capitalize(): key, "MPG": value})
                        #f.write("{}: {}\n".format(key,value))
            else:
                for key, value in printable:
                        print("{}: {}\n".format(key,value))

def plot_result(res, x_axis):
    plt.xlabel(x_axis)
    plt.ylabel("MPG")
    plt.xticks(rotation = 90)
    plt.plot(list(res.keys()), list(res.values()))
    plt.show()

if __name__ == "__main__":
    args = parser(argv[1:])
    a = AutoMPGData()
    print(args)
    if args.command == "print":
        match args.sortOrder:
            case "year":
                a.sort_by_year()
            case "mpg":
                a.sort_by_mpg()
            case _:
                a.sort_by_default()
        toPrint(a, args.outputFile, args.command)

    elif args.command == "mpg_by_year":
        res = a.mpg_by_year()
        if args.do_plot: 
            plot_result(res, (args.command.split("_")[2]).capitalize())
        res = dict(sorted(res.items()))
        toPrint(res.items(), args.outputFile, args.command)
    elif args.command == "mpg_by_make":
        res = a.mpg_by_make()
        if args.do_plot: 
            plot_result(res, (args.command.split("_")[2]).capitalize())
        res = dict(sorted(res.items()))
        toPrint(res.items(), args.outputFile, args.command)