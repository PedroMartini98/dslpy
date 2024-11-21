
price = 50

while price > 0:
    coin = input('Insert coin: ')
    coin = int(coin)
    if coin == 50 or coin == 25 or coin == 10 or coin == 5:
        price = price - coin
        if price>0:
            print(f"Amount due: {price}")
    else:
        print("We only accept coins of fifty,twenty five and five cents! Try again!")
        
price = abs(price)
print(f"Change Owed: {price}")