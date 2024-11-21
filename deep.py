answer = input("What's the answer for the exercise? ").lower().strip()

if answer == '42' or answer == 'forty two' or answer == 'forty-two' or answer == 'forty_two':
    print('yes')
else:
    print('no')