#pylint: disable = C0114
#pylint: disable = C0116

import prime_using_composite


def prime_in_range():

    start = int(input("Enter the starting point: "))
    end = int(input("Enthr the last point: "))

    X = 1

    for X in range(start, end+1):
        if prime_using_composite.prime(X):
            print(X)
