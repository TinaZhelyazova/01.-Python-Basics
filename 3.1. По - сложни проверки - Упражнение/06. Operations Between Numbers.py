a=int(input())
b=int(input())
operator =input()
result=0
type=""
is_valid=True


if operator =="+":
    result=a+b
    if result%2==0:
        type="even"
    else:
        type="odd"
elif operator =="-":
    result=a-b
    if result%2==0:
        type="even"
    else:
        type="odd"
elif operator == "*":
    result=a*b
    if result%2==0:
        type="even"
    else:
        type="odd"
elif operator =="/":
    if a==0 or b==0:
        is_valid=False
    elif is_valid==True:
        result = a/b
elif operator == "%":
    if a == 0 or b == 0:
        is_valid = False

    if is_valid == True:
        result = a % b


if operator=="+" or operator=="-" or operator=="*":
    print(f"{a} {operator} {b} = {result} - {type}")
elif not is_valid:
    print(f"Cannot divide {a} by zero")
elif operator=="/":
    print(f"{a} / {b} = {result:.2f}")
elif operator=="%":
    print(f"{a} % {b} = {result}")




