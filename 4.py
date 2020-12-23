number = int(input("Enter your number: "))
max = 0

while number!=0:
    if number % 10 >= max:
        max = number % 10
        number //= 10
    else:
        break
print (f"The biggest number is {max}")