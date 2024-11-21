import random
import sys

while True:
    try:
        number = input('Level? ')
        if int(number) >= 2:
            break
    except:
        pass
answer = random.randint(1,int(number))

while True:
    try:
        guess = input("Guess: ")
        if int(guess) > 0:
            if int(guess) == answer:
                print("Just right!")
                break              
            elif int(guess) > answer:
                print('Too large!')
            elif int(guess) < answer:
                print('Too small!')
    except:
        pass


sys.exit()