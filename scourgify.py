import sys
import csv

def main():
    check_clia()
    table=[]
    try:
        with open(sys.argv[1],'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                last,first = row["name"].split(',')
                table.append({'first':first,"last":last,"house":row["house"]})
    except FileNotFoundError:
        sys.exit("File does not exist")
    with open(sys.argv[2],'w') as newfile:
        writer = csv.DictWriter(newfile,fieldnames=["first","last","house"])
        writer.writerow({"first":"first","last":"last","house":"house"})
        for row in table:
            writer.writerow({"first":row["first"],"last":row["last"],"house":row["house"]})

def check_clia():
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit()
    elif len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit()

    elif ".csv" not in sys.argv[1] and ".csv" not in sys.argv[2]:
        print("Not a csv file")
        sys.exit()

if __name__ == "__main__":
    main()