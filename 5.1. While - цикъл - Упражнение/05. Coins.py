sum_of_change = float(input())
sum_of_change = sum_of_change*100
coin_counter = 0
coins = 0

while int(sum_of_change) != 0:
    if sum_of_change >= 200:
        sum_of_change -= 200
    elif sum_of_change >= 100:
        sum_of_change -=100
    elif sum_of_change >= 50:
        sum_of_change -= 50
    elif sum_of_change >= 20:
        sum_of_change -=20
    elif sum_of_change >= 10:
        sum_of_change -= 10
    elif sum_of_change >= 5:
        sum_of_change -= 5
    elif sum_of_change >= 2:
        sum_of_change -=2
    elif sum_of_change >= 1:
        sum_of_change -= 1

    coins += 1
print(coins)