
fruits = {"apple" : 130,
"avocado" : 50,
"banana" : 110,
"cantaloupe" : 50,
"grapefruit" : 60,
"grapes" : 90,
"honeydew_melon" : 50,
"kiwifruit" : 90,
"lemon" : 15,
"lime"  :20,
"nectarine" : 60,
"orange" : 80,
"peach" : 60,
"pear" : 100,
"pineapple" : 50,
"plums" : 70,
"srawberries" : 50,
"sweet_cherries" : 100,
"tangerine" : 50,
"watermenlon" : 80}

fruit_asked = input("What's the fruit? ")

for key in fruits:
    if key == fruit_asked.lower():
        print(f"Calories: {fruits[key]}")
