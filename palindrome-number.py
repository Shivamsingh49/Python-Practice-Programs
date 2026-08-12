num = int(input("Enter the num: "))
dup = num
reverse = 0
place = 10 ** (len(str(num)) -1)
while num > 0:
    rem = num % 10
    reverse = reverse + rem * place
    place = place // 10
    num = num // 10
if reverse == dup:
    print("Palindrome")
else:
    print("Not a Palindrome")