#pylint: disable = C0114


def prime_in_range():

    start = int(input("Enter the starting point: "))
    end = int(input("Enthr the last point: "))

    x = 1

    for x in range(start, end+1):
        if prime_using_composite.prime(x):
            return x


print(prime_in_range())
