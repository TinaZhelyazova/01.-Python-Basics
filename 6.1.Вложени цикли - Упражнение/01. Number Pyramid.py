number = int(input())
current = 1
is_current_bigger_than_n = False

for i in range(1, number+1, 1):
    for j in range(1, i+1):
        if current > number:
            is_current_bigger_than_n = True
            break
        print(current, end=" ")
        current += 1
    if is_current_bigger_than_n:
        break
    print()
