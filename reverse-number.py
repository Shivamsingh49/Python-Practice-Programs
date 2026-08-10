# Reverse the number
num = int(input("Enter the num: "))
reverse = 0
place = 10 ** (len(str(num))-1)
while num > 0:
    rem = num % 10
    reverse = reverse + rem * place
    place = place // 10
    num = num // 10

print(reverse)