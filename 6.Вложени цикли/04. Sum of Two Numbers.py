start_of_interval = int(input())
end_of_interval = int(input())
magic_number = int(input())
count = 0
result = 0

for i in range(start_of_interval, end_of_interval+1):
    for j in range(start_of_interval, end_of_interval+1):
        result = i+j
        count += 1
        if result == magic_number:
            print(f"Combination N:{count} ({i} + {j} = {magic_number})")
            break
    if result == magic_number:
        break

if result != magic_number:
    print(f"{count} combinations - neither equals {magic_number}")
