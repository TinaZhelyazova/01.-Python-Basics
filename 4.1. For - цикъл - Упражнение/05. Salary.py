n = int(input())
salary = int(input())

for i in range(n):
    current_site = (input())
    if current_site=="Facebook":
        salary = salary - 150
    elif current_site=="Instagram":
        salary = salary - 100
    elif current_site =="Reddit":
        salary = salary - 50

    if salary<=0:
        print("You have lost your salary.")
        break;
if salary>0:
    print(salary)

