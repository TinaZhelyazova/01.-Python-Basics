import sys

n = int(input())
result = 0
max_num = -sys.maxsize

for i in range(n):
    current_num = int(input())

    if current_num > max_num:
        max_num = current_num
    result += current_num

result = result-max_num

if max_num == result:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    diff=abs(result-max_num)
    print("No")
    print(f"Diff = {diff}")


