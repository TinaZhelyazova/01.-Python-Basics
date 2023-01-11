number = int(input())
bonus =0
second_bonus=0

if number>= 1000:
    bonus = number* (10/100)
elif number> 100:
    bonus = number *(20/100)
elif number<=100:
    bonus = 5



if number%2==0:
   second_bonus=1
elif number%5 ==0:
    second_bonus=2;

bonuses=bonus+second_bonus
number_with_bonus = number+bonus+second_bonus


print(bonuses)
print(number_with_bonus)
