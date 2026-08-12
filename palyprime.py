num = int(input("Enter the num: "))
if num > 1:
    for val in range(2, int(num ** 0.5)+1):
        if num % val == 0:
            print("Not a Palyprime")
            break
    else:
        reverse = 0
        dup = num
        while num > 0:
            rem = num % 10
            reverse = reverse * 10 + rem
            num = num // 10
        if  reverse == dup:
            print("Palyprime Number")
        else:
            print("Not a Palyprime Number")
else:
    print("Not a Palyprime Number")
