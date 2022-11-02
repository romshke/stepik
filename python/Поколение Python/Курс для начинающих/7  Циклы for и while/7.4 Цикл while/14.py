coins = 0
price = int(input())

while price - 25 >= 0: 
    price -= 25
    coins += 1
while price - 10 >= 0:
    price -= 10
    coins += 1
while price - 5 >= 0: 
    price -= 5
    coins += 1
while price - 1 >= 0: 
    price -= 1
    coins += 1
print(coins)