#pylint: disable = C0114
#pylint: disable = C0116

import prime_using_composite


def prime_in_range():

    START = int(input("Enter the starting point: "))
    END = int(input("Enthr the last point: "))

    TEMP = 1

    for TEMP in range(START, END+1):
        if prime_using_composite.prime(TEMP):
            print(TEMP)
