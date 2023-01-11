budget = float(input())
season = input()
destination ="" #Bulgaria, Balkans or Europe
where ="" #camp or hotel
expenses=0

if budget <=100:
    destination="Bulgaria"
    if season=="summer":
        expenses = budget*0.3
        where="Camp"
    elif season=="winter":
        expenses = budget*0.7
        where = "Hotel"
elif budget <=1000:
    destination = "Balkans"
    if season == "summer":
        expenses = budget * 0.4
        where = "Camp"
    elif season == "winter":
        expenses = budget * 0.8
        where = "Hotel"
elif budget >1000:
    destination = "Europe"
    where = "Hotel"
    expenses = budget*0.9

print(f"Somewhere in {destination}")
print(f"{where} - {expenses:.2f}")

