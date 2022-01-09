n = int(input())

if n >= 1 and n <= 100:
    if n == range(2,6) and n%2 == 0:
        print("Not Wierd")
    elif n == range(6,21) and n%2 == 0:
        print("Wierd")
    elif n > 20 and n%2 == 0:
        print("Not Wierd")
    else:
        print("Wierd")