from datetime import date
import re
import sys
import inflect

p = inflect.engine()


def main():
    bday = input("Date of birth: ")
    try:
        year,month,day = check_bday(bday)
        print(year,month,day)
    except:
        sys.exit("Invalid Date")
    bday_int = date(int(year),int(month), int(day))
    today = date.today()
    diff = today - bday_int 
    total_minutes = diff.days * 24 * 60
    output = p.number_to_words(total_minutes, andword="")
    print(output.capitalize()+" minutes")

def check_bday(bd):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", bd):
        year,month,day = bd.split("-")
        return year,month,day


if __name__ == "__main__":
    main()