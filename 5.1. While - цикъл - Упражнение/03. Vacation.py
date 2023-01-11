money_needed_for_vacation = float(input())
money_available = float(input())
action = input()
money_for_action = float(input())
action_counter = 0 #day counter
saving = True
spend_counter = 0

while saving:
    if action == "spend":
        if money_for_action >= money_available:
            money_available = 0
        else:
            money_available = money_available - money_for_action
        action_counter += 1
        spend_counter += 1
        if spend_counter == 5:
            print("You can't save the money.")
            print(f"{action_counter}")
            break
    elif action == "save":
        money_available = money_available + money_for_action
        spend_counter = 0
        action_counter += 1
    if money_available >= money_needed_for_vacation:
        print(f"You saved the money for {action_counter} days.")
        break
    action = input()
    money_for_action = float(input())



