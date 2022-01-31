import math


def prime(num):

    flag = False
    if num > 1:
        for i in range(2, math.floor(math.sqrt(num)+1)):
            if (num % i) == 0:
                flag = True
            break

    if flag:
        return f"{num} is not a prime number"

    else:
        return f"{num} is a prime number"


print(prime(int(input("Enter a number: "))))
