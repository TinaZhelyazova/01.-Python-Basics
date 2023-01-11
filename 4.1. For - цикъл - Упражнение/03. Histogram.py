n = int(input())
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0

for i in range(n):
    current_num = int(input())
    if current_num >= 800:
        n5 =n5+ 1
    elif current_num < 200:
        n1 =n1+1
    elif current_num <= 200 or current_num <= 399:
        n2 =n2+1
    elif current_num <= 400 or current_num <= 599:
        n3 =n3+ 1
    elif current_num <= 600 or current_num <= 799:
        n4 =n4+ 1



print(f"{(n1/n)*100:.2f}%")
print(f"{(n2/n)*100:.2f}%")
print(f"{(n3/n)*100:.2f}%")
print(f"{(n4/n)*100:.2f}%")
print(f"{(n5/n)*100:.2f}%")
