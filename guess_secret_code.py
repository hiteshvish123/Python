import random

x = int(input("Enter the lower limit: "))
y = int(input("Enter the upper limit: "))

if y<x:
    decider = input("""Upper limit cannot be smaller than lower limit
    Change lower limit -> x
    Change upper limit -> y""")

secret_number = random.randint(x, y)

#guess_count = 0
#guess_limit = 3
#while i < 3: