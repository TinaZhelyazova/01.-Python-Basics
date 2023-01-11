number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_veggie_menus = int(input())

chicken_menu = 10.35
fish_menu = 12.40
veggie_menu = 8.15
delivery = 2.5

chicken_price = number_of_chicken_menus*chicken_menu
fish_price = number_of_fish_menus*fish_menu
veggie_price = veggie_menu*number_of_veggie_menus
all_menus_price = chicken_price+fish_price+veggie_price
dessert = (20/100)*all_menus_price

all_price = all_menus_price+dessert+delivery
print(all_price)