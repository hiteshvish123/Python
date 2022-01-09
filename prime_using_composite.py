import math

num = int(input("Enter a number: "))
flag = False

if num>1:
    for i in range(2,math.floor(math.sqrt(num)+1)):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is not a prime number")

else:
    print(num, "is a prime number")