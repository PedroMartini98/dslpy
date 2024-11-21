import random


def main():
    level = get_level()
    rounds = 0
    score = 0
    while rounds < 10:
        
        if simulate_round(level):
            score +=1
        rounds +=1
                
    print("Score: ", score,"/10")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0 and level < 4:
                break        
        except:
            pass
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(1,9)
        y = random.randint(1,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y

def simulate_round(level):
    tries = 0
    x,y = generate_integer(level)
    while tries < 3:
        try:   
            answer = x + y
            guess = int(input(f"{x}+{y}= "))
            if guess == answer:
                return True
            elif guess != answer:
                tries +=1
                print('EEE')
                
        except:
            tries += 1
            print('EEE')

    print(f"{x}+{y}=", answer)
    return False
if __name__ == "__main__":
    main()