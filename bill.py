units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100)
else:
    bill = (100 * 5) + (100 * 7) + (units - 250) * 10
print("electricity bill")
