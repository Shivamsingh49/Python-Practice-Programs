num = int(input("Enter the number: "))
dup = num
length = len(str(num))
res = 0
while num > 0:
    rem = num % 10
    res = res + rem ** length
    num = num // 10
if res == dup:
    print("Armstrong Number")
else:
    print("Not an Armstrong number")


