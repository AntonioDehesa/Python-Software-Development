import sys

def read_arguments(): 
    for x in sys.argv[1::]:
        print(x)

if __name__ == "__main__":
    read_arguments()