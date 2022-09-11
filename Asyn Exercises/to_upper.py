import sys

def read_arguments(): 
    print("Please write something in this program.")
    while True: 
        user_input = input().upper()
        if "QUIT" in user_input:
            print("Bye!", file=sys.stderr)
            break
        print(user_input)

if __name__ == "__main__":
    read_arguments()