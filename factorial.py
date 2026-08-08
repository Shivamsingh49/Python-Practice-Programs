# Using for loop
num = int(input("Enter the input: "))
res = 1
for val in range(1, num+1):
    res *= val
print(f"The factorial of {num} is {res}")



# Using while loop
num = int(input("Enter the number: "))
res = 1
val = 1
while val <= num:
    res *= val
    val += 1
print(f"The factorical of {num} is {res}")



# Using function
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
    
n = int(input("Enter the number: "))
result = fact(n)
print(result)


