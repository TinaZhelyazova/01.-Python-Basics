type = input()
r = int(input())
c = int(input())
ticket_price=0
area=r*c

if type == "Premiere":
    ticket_price=12
elif type =="Normal":
    ticket_price=7.50
elif type == "Discount":
    ticket_price=5

income = ticket_price*area
print(f"{income:.2f} leva")