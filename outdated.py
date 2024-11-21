valid_months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        month,day,year = date.split('/')
        if (int(month)>=1 and int(month)<=12) and (int(day)>=1 and int(day)<=31) and (len(year)==4):
            break
    except:
        try:
            old_month,old_day,year = date.split(' ')
            for i in range(len(valid_months)):
                if old_month.capitalize() == valid_months[i]:
                    month = i + 1
            day = old_day.replace(',','')
            if (int(month)>=1 and int(month)<=12) and (int(day)>=1 and int(day)<=31) and (len(year)==4):
                break
        except:
            pass 

print(f"{year}-{int(month):02}-{int(day):02}")