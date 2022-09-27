money = int(input())
money = 1000 - money

coins = [500, 100, 50, 10, 5, 1]
sol = 0

for coin in coins:
    a = money // coin
    money = money - a * coin
    sol += a

print(sol)