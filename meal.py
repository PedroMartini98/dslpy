def main():
    ...     
    time = input("What time is it? ")
    time = convert(time)
    if 7 <= time <= 8:
        print("It's breakfast time!")
    elif 12 <= time <= 13:
        print("It's lunch time!")
    elif 18 <= time <= 19:
        print("It's dinner time!")



def convert(time):
    ... 
    hours,minutes = time.split(':')
    minutes = float(minutes) /60
    return float(hours)+minutes


if __name__ == "__main__":
    main()