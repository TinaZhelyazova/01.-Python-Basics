flower = input()
number_of_flowers = int(input())
budget = int(input())
price=0

if flower == "Roses":
    price=5
elif flower =="Dahlias":
    price=3.8
elif flower =="Tulips":
    price=2.8
elif flower == "Narcissus":
    price=3
elif flower =="Gladiolus":
    price=2.5

sum=number_of_flowers*price

if number_of_flowers>80 and flower=="Roses":
    sum = sum-(sum*0.1)
elif number_of_flowers>90 and flower == "Dahlias":
    sum = sum-(sum*0.15)
elif number_of_flowers>80 and flower == "Tulips":
    sum = sum-(sum*0.15)
elif number_of_flowers<120 and flower == "Narcissus":
    sum = sum+(sum*0.15)
elif number_of_flowers<80 and flower == "Gladiolus":
    sum = sum+(sum*0.20)

if budget>=sum:
    money_left=budget-sum
    print(f"Hey, you have a great garden with {number_of_flowers} {flower} and {money_left:.2f} leva left.")
else:
    money_needed= sum-budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")

