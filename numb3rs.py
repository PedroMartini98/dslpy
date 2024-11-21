import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
   valid = re.search(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$",ip)
   if valid:
       list_of_numbers = ip.split(".")
       for number in list_of_numbers:
           if int(number) < 0 or int(number) > 255:
               return True
           return False
   else:
       return False


...


if __name__ == "__main__":
    main()