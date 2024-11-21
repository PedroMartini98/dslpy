import sys
import csv
from tabulate import tabulate

def main():
    check_clia()
    table=[]
    try:
        with open(sys.argv[1],'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(tabulate(table[1:],headers=table[0],tablefmt="grid"))


def check_clia():
    if len(sys.argv) > 2:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) < 2:
        print("Too many command-line arguments")
        sys.exit()

    elif ".csv" not in sys.argv[1]:
        print("Not a csv file")
        sys.exit()

if __name__ == "__main__":
    main()