yearly_tax = int(input())
shoes = yearly_tax-(yearly_tax * 40/100)
equipment = shoes - (shoes*20/100)
ball = (1/4)* equipment
accesories = (1/5)*ball

all_expenses = yearly_tax+shoes+equipment+ball+accesories
print(all_expenses)