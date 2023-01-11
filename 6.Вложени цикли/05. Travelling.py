destination = input()
min_budget = float(input())
savings = 0

while destination != "End":
    saved_money = float(input())
    savings += saved_money
    if savings >= min_budget:
        print(f"Going to {destination}!")
        savings = 0
        destination = input()
        if destination!="End":
            min_budget = float(input())
        else:
            break


