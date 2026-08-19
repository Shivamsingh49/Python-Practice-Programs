'''EMIRP Number: 
An EMIRP is a prime number that results in different valid prime when its decimal digits are reversed.
Rule:
- Num must be prime.
- Cannot be a palindrome when reversed.
- Must be a prime when reversed. '''

num = int(input("Enter the num: "))
if num > 1:
    for val in range(2, int(num ** 0.5)+1):
        if num % val == 0:
            print("Not EMIRP Number")
            break

    else:
        rev = 0
        dup = num
        while num > 0:
            rem = num % 10
            rev = rev * 10 + rem
            num = num // 10

        if dup != rev:
            if rev > 1:
                for val in range(2, int(num ** 0.5)+1):
                    if rev % val == 0:
                        print("Not EMIRP Number")
                        break
                else:
                    print("EMIRP Number")
        else:
            print("Not EMIRP Number")
            
else:
    print("Not Emirp Number")



