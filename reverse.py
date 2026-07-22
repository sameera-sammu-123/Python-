


num = int(input("Enter a number: "))

original = num

reverse = 0
while num > 0:
    digit = num % 10

    reverse = reverse * 10

    reverse = reverse + digit

    
    num = num // 10


print("Original Number =", original)


print("Reverse Number =", reverse)
''''''


a=input('')
count=0
for i in range in a:
    if 1%2 ==0:
        count=count+1
        print(" even digit",count)
    else:
        count=count+1
        print("odd digit",count)
        
