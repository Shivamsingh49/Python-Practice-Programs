# Using for loop
num = int(input("Enter the num: "))
res = 0
for val in range(1, num//2 +1):
    if num % val == 0:
        res += val
if res == num:
    print("Perfect number")
else:
    print("Not a perfect number")



# Using while loop
num = int(input("Enter the num: "))
res = 0
val = 1
while val <= num//2:
    if num % val == 0:
        res += val
    val += 1
if res == num:
    print("Perfect number")
else:
    print("Not a perfect number")
