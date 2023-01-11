budget = float(input())
number_video_cards = int(input())
number_processors = int(input())
number_ram = int(input())

video_cards_bought =250*number_video_cards

video_card_price=250
processor_price=0.35*video_cards_bought
ram_price=0.10*video_cards_bought

processrs_bought = number_processors*processor_price
ram_bought = number_ram*ram_price

total = video_cards_bought+processrs_bought+ram_bought

if number_video_cards> number_processors:
    total = total-(total*0.15)

if budget>= total:
    money_left= budget-total
    print(f"You have {money_left:.2f} leva left!")
else:
    money_needed= total-budget
    print(f"Not enough money! You need {money_needed:.2f} leva more!")
