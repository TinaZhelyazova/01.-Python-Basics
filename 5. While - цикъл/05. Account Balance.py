transaction = input()

balance = 0

while transaction != "NoMoreMoney":
    if float(transaction) < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {float(transaction):.2f}")
    balance = balance + float(transaction)
    transaction = input()
print(f"Total: {balance:.2f}")
