trip_price = float(input())
num_of_puzzels=int(input())
num_of_dolls=int(input())
num_of_bears=int(input())
num_of_minions=int(input())
num_of_trolly=int(input())

price_of_puzzle = 2.60
price_of_doll = 3
price_of_bear = 4.10
price_of_minion = 8.20
price_of_trolly = 2

bought_puzzles = num_of_puzzels*price_of_puzzle
bought_dolls = num_of_dolls*price_of_doll
bought_bears = num_of_bears*price_of_bear
bought_minions = num_of_minions*price_of_minion
bought_trollies = num_of_trolly*price_of_trolly

number_of_all_toys = num_of_puzzels+num_of_dolls+num_of_bears +num_of_minions+num_of_trolly
sum_of_all = bought_puzzles+bought_dolls+bought_bears+bought_minions+bought_trollies

if number_of_all_toys>=50:
    sum_of_all = sum_of_all-(sum_of_all*(25/100))

money_after_rent = sum_of_all - (sum_of_all*(10/100))

if money_after_rent>=trip_price:
    money_left = money_after_rent-trip_price
    print(f"Yes! {money_left:.2f} lv left.")
elif money_after_rent<trip_price:
    money_needed = trip_price - money_after_rent
    print(f"Not enough money! {money_needed:.2f} lv needed.")



