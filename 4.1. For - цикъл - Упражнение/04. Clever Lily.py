age = int(input())
price_washing_machine = float(input())
price_of_toy = int(input())
toys = 0
money = 0
previous_money=0


for i in range(1, age+1):
    if i%2 ==0:
        if i ==2:
            money = 10
            previous_money = money
        else:
            money = 10+previous_money + money
            previous_money = previous_money+10
        money = money-1
    else:
        toys = toys+1

money_from_toys = toys*price_of_toy
money = money+money_from_toys

if money>= price_washing_machine:
    diff = money - price_washing_machine
    print(f"Yes! {diff:.2f}")
else:
    diff=price_washing_machine-money
    print(f"No! {diff:.2f}")



