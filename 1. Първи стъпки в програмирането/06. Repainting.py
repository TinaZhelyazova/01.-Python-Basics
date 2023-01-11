nylon_needed = int(input())
paint_needed=int(input())
thinner_needed = int(input())
hours_of_work = int(input())

nylon_price = 1.50
paint_price = 14.50
thinner_price = 5

first_addition = paint_needed + (paint_needed*(10/100))
second_addition = nylon_needed +2
bags = 0.4
money_for_materials = bags+ (second_addition*nylon_price)+(paint_price*first_addition)+(thinner_price*thinner_needed)
money_for_one_hour_for_workers = money_for_materials*(30/100)
money_for_workers = money_for_one_hour_for_workers*hours_of_work

sum_result = money_for_materials +money_for_workers

print(sum_result)

