def main():
    fraction = input("Fraction: ")
    converted_fraction = convert(fraction)
    output= gauge(converted_fraction)
    print(output)



def convert(fraction):
    while True:
        try:
            x,y= fraction.split('/')
            x = int(x)
            y = int(y)
            f = x/y
            if f <=1:
                p = int(f*100)
                return p
            else:
                fraction = input("Fraction: ")
                pass 
        except(ValueError,ZeroDivisionError):
            raise
        

def gauge(p):
    if p <= 1:
        return 'E'
    elif p >= 99:
        return 'F'
    else:
        return f"{p}%"


if __name__ == "__main__":
    main()