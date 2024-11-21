import sys

def main():
    check_clia()
    try:
        file = open(sys.argv[1],"r")
        lines = file.readlines()
        count = 0

        for line in lines:

            if is_line_not_useful(line) == False:
                count += 1
                
        
        print(count)

    except FileNotFoundError:
        sys.exit('File does not exist!')

def check_clia():
    if len(sys.argv) > 2:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) < 2:
        print("Too many command-line arguments")
        sys.exit()

    elif ".py" not in sys.argv[1]:
        print("Not a python file")
        sys.exit()
def is_line_not_useful(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False
if __name__ == "__main__":
    main()