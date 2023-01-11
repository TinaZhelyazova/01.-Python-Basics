budget = float(input())
statists = int(input())
price_of_clothing_for_one_statist =float(input())
decor =0

decor = budget*0.10
price_of_all_clothing = price_of_clothing_for_one_statist*statists
if statists >=150:
    price_of_all_clothing = price_of_all_clothing-(price_of_all_clothing*0.10)

all_money_needed =decor+price_of_all_clothing

if all_money_needed>budget:
    money_needed = all_money_needed-budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
else:
    money_left = budget-all_money_needed
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")

