boxes_pens = int(input())
boxes_of_markers = int(input())
liters_cleaning_liquid=int(input())
discount = int(input())

pens_price = 5.80 *boxes_pens
markers_price = 7.20 *boxes_of_markers
cleaning_liquid_price_per_liter = 1.20 *liters_cleaning_liquid


all_items_price = pens_price + markers_price +cleaning_liquid_price_per_liter
money_needed =  all_items_price- (all_items_price*(discount/100))
print(money_needed)