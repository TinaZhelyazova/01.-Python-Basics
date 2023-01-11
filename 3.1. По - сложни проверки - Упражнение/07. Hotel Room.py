month = input()
nights = int(input())
room=""
price_for_studio =0
price_for_apartment =0

if month=="May" or month=="October":
    price_for_studio=50
    price_for_apartment=65
    if nights>7 and nights<=14:
        price_for_studio= price_for_studio-(price_for_studio*0.05)
    elif nights>14:
        price_for_studio= price_for_studio-(price_for_studio*0.30)
        price_for_apartment=price_for_apartment-(price_for_apartment*0.1)
elif month=="June" or month=="September":
    price_for_studio=75.2
    price_for_apartment=68.7
    if nights > 14:
        price_for_studio = price_for_studio - (price_for_studio * 0.20)
        price_for_apartment = price_for_apartment - (price_for_apartment * 0.1)
elif month=="July" or month=="August":
    price_for_studio=76
    price_for_apartment=77
    if nights > 14:
        price_for_apartment = price_for_apartment - (price_for_apartment * 0.1)

whole_price_apartment=price_for_apartment*nights
whole_price_studio=price_for_studio*nights

print(f"Apartment: {whole_price_apartment:.2f} lv.")
print(f"Studio: {whole_price_studio:.2f} lv.")