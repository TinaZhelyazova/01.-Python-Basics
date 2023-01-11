n = int(input())

first_sum = 0
second_sum = 0

for i in range(n*2):
    current_num = int(input())
    if i < (n*2)/2:
        first_sum += current_num
    else:
        second_sum += current_num

if first_sum == second_sum:
    print(f"Yes, sum = {first_sum}")
else:
    diff = abs(first_sum-second_sum)
    print(f"No, diff = {diff}")
