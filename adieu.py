import inflect

p = inflect.engine()

names=[]

while True:
    name = input("Name: ")
    if name.lower() == 'done':
        break
    else:
        names.append(name)

out = p.join(names)
print("Adieu, adieu, to", out)