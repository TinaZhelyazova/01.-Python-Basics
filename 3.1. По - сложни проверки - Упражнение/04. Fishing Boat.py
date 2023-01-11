budget = int(input())
season = input()
fisherman = int(input())
price =0

if season=="Spring":
    price = 3000
elif season=="Summer" or season =="Autumn":
    price=4200
elif season=="Winter":
    price=2600

if fisherman<=6:
    price = price - (price*0.1)
elif fisherman>=12:
    price = price-(price*0.25)
elif fisherman>=7 or fisherman<=11:
    price = price-(price*0.15)

if fisherman%2==0 and (season == "Spring" or season=="Summer" or season=="Winter"):
    price = price-(price*0.05)

if budget>=price:
    money_left = budget-price
    print(f"Yes! You have {money_left:.2f} leva left.")
elif price>budget:
    money_needed = price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")
