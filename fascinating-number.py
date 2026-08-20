'''
Fascinating Number:
- A fascinating number is a number that forms a special 9-digit sequence containing all digits from 1 through 9 exactly 
    once when it is multiplied by 2 and 3, and then concatenated with the original number.
'''
num = int(input("Enter the num: "))
ans = str(num * 1) + str(num * 2) + str(num * 3)

for val in range(1, 10):
    if str(val) not in ans:
        print("Not a Fascinating Number.")
        break

else:
    print("Fascinating Number")


