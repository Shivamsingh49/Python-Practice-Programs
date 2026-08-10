# Spy number
num = int(input("Enter the num: "))
sum = 0
mul = 1
while num > 0:
    rem = num % 10
    sum += rem
    mul *= rem
    num = num // 10
if sum == mul:
    print("Spy Number")
else:
    print("Not a Spy number")