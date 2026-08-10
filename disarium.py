num = int(input("Enter the num: "))
dup = num
total = 0
power = len(str(num))
while num > 0:
    rem = num % 10
    total += rem ** power
    num = num // 10
    power -= 1

if total == dup:
    print(f"{dup} is Disarium Number")
else:
    print(f"{dup} is not Disarium Number")