
balance = 10000   # initial balance

withdraw = int(input("Enter withdrawal amount: "))

if withdraw <= balance:
    balance = balance - withdraw
    print("Withdrawal successful!")
    print("Remaining Balance =", balance)
else:
    print("Insufficient Balance")
