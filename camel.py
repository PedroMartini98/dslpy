text = input('camelCase: ')

print('snake_case: ', end="")

for char in text:
    if char.isupper():
        print('_', end="")
        print(char.lower(),end="")
    elif char.islower():
        print(char,end="")


