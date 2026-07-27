# Convert Integer to Binary
# num = int(input("Enter the number: "))
# res = 0
# place = 1
# while num > 0:
#     rem = num % 2
#     res = res + rem * place
#     place = place * 10
#     num = num // 2
# print(res)


# Convert Binary to Integer
num = 1101
res = 0
power = 0
while num > 0:
    rem = num % 10
    res = res + rem * (2 ** power)
    power += 1
    num = num // 10
print(res)

