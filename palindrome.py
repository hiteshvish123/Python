NUMBER = int(input("Enter a number: "))

N = NUMBER
REV = 0
while NUMBER != 0:
    REM = NUMBER % 10
    NUMBER = NUMBER // 10
    REV = REV * 10 + REM

if REV == N:
    print("PALINDROME")
else:
    print("NOT PALINDROME")
