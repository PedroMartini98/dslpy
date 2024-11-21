def main():
    greeting = input('Greeting:').lower().strip() 

    print(greeting(greeting))

def greeting(greeting):
    if greeting.startswith('hello'):
        return('$0')
    elif greeting.startswith('h'):
        return('$20')
    else:
        return('$100')
    
if __name__ == "__main__":
    main()