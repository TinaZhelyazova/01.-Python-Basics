city=(input())
sales = float(input())
comission =0
is_valid=True

if sales>10000:
    if city=="Sofia":
        comission=0.12
    elif city=="Varna":
        comission=0.13
    elif city=="Plovdiv":
        comission=0.145
    else:
        is_valid=False
elif 1000<sales<=10000:
    if city=="Sofia":
        comission=0.08
    elif city=="Varna":
        comission=0.10
    elif city=="Plovdiv":
        comission=0.12
    else:
        is_valid=False
elif 500<sales<=1000:
    if city=="Sofia":
        comission=0.07
    elif city=="Varna":
        comission=0.075
    elif city=="Plovdiv":
        comission=0.08
    else:
        is_valid=False
elif 0<=sales<=500:
    if city=="Sofia":
        comission=0.05
    elif city=="Varna":
        comission=0.045
    elif city=="Plovdiv":
        comission=0.055
    else:
        is_valid=False
else:
    is_valid=False




if is_valid==False:
    print("error")
else:
    money_after_comission = sales * comission
    print(f"{money_after_comission:.2f}")