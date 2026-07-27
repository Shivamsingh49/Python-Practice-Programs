# Using for loop
num = int(input("Enter the number: "))
if num > 1:
    for val in range(2, int(num ** 0.5) + 1):
        if num % val == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


# Using while loop
num = int(input("Enter the number: "))
val = 2
while val < num:
    if num%val == 0:
        print(f"{num} is not a Prime number")
        break 
    val += 1
else:     
    print(f"{num} is a Prime number")