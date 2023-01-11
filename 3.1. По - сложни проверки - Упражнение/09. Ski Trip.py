days = int(input())
room = input()
grade = input()
discount=0
price_for_room_for_one_person=18 *(days-1)
price_for_apartment=25* (days-1)
price_for_president_apartment=35 * (days-1)
sum=0

if days<10:
    if room=="room for one person":
        discount =0
        sum = price_for_room_for_one_person
    elif room == "apartment":
        discount = 0.3*price_for_apartment
        sum = price_for_apartment - discount
    elif room == "president apartment":
        discount = 0.1*price_for_president_apartment
        sum = price_for_president_apartment - discount
elif days>15:
    if room=="room for one person":
        discount =0
        sum=price_for_room_for_one_person
    elif room == "apartment":
        discount = 0.50*price_for_apartment
        sum = price_for_apartment - discount
    elif room == "president apartment":
        discount = 0.20*price_for_president_apartment
        sum = price_for_president_apartment -discount
elif days>=10 or days<=15:
    if room=="room for one person":
        discount =0
        sum = price_for_room_for_one_person
    elif room == "apartment":
        discount = 0.35*price_for_apartment
        sum = price_for_apartment - discount
    elif room == "president apartment":
        discount = 0.15*price_for_president_apartment
        sum = price_for_president_apartment - discount


if grade == "positive":
    sum = sum+(sum*0.25)
elif grade =="negative":
    sum = sum-(sum*0.10)

print(f"{sum:.2f}")
