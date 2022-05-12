#pylint: disable = C0114
#pylint: disable = C0116


# List creation
EMPTY_LIST = []  # An empty lsit
NUMBERS = [2, 212, 313]
LETTERS = ["M", "D", "H"]
NORMAL_LIST = [1, 2, 3, "A", "B", "C"]  # A list with multiple datatypes
MATRIX = [[1, 2], [2, 3]]  # A 2x2 matrix or 2-dimensional list
ZEROS = [0] * 50  # A list of 50 zeros
COMBINED = NUMBERS + LETTERS  # lIST CONCATENATION
print(COMBINED)
# A sequence of numbers using list fn. which accepts an iterable as an argument
SEQUENCE = list(range(20))
print(SEQUENCE)
# Each character is tearted as an element of list after iteration
CHARS = list("HELLO world")
print(CHARS)
print(len(CHARS))  # Returns length of CHARS variable


# Accessing items in lists
print(LETTERS[0])  # print at index 0
print(LETTERS[-1])  # print at index -1
LETTERS[0] = "esfs"  # Lists are mutable
print(LETTERS)
print(NORMAL_LIST[0: 2])  # Slicing the list
# Every alternate element in the list will be printed on the terminal
print(SEQUENCE[::2])
print(SEQUENCE[::-1])  # print the same list in reverse order


# Unpacking list
# conventional method of assigning individual elements to different variables
FIRST = SEQUENCE[0]
SECOND = SEQUENCE[1]
THIRD = SEQUENCE[2]
# Here the list should have only 3 elements i.e. no of elements in list to be unpacked should be equal to the number of variables
first, second, third = NUMBERS
print(first)
# Here the no of variable do not matter as only the first element is being unpacked to First variable, rest all the elements are being packed to the *Other named list
First, *Other, Last = SEQUENCE
print(First)
print(Other)
print(Last)


# Looping over list
for letter in LETTERS:
    print(letter)
# Enumerate object will return an emumerte object which is iterable with index of each element in the list
for letter in enumerate(LETTERS):
    print(letter)  # this and the latter statement is exactly same
    print(letter[0], letter[1])

# The simpler way to do the above work is using the unpacking method
# Unpack the enumerate objects(tuple) to two different variables then print them
LIST1 = ['a', 'b', 'c', 'd']
for index, letter in enumerate(LIST1):
    print("Unpacking tuple using emumerate:", index, letter)


# Adding or removing items to/from list
# Add
LIST1.append("e")  # add at the end of list
LIST1.insert(0, '-')  # add at index
print(LIST1)
# Remove
LIST1.pop()  # remove from the end of the list
LIST1.pop(0)  # removes at element at index
# removes element whose index is not known, only removes 1st element if multiple occurances of "b"
LIST1. remove("b")
print(LIST1)
del LIST1[0:2]  # deletes the elements over a range of index in list
print(LIST1)
LIST1.clear()  # clears the list
print(LIST1)


# Sorting List
numberss = [2, 3, 4, 5, 6, 6, 6, 7, 67, 87]
print(numberss.sort)
print(numberss.sort(reverse=True))
print(sorted(numberss))
print(sorted(numberss, reverse=True))
print(numberss)
# Sort Numeric List
nums = [1, 5, 3, 4, 2, 10, 6, 8, 7, 9]
nums.sort()
print('List in Ascending Order: ', nums)
nums.sort(reverse=True)
print('List in Descending Order: ', nums)
# Sort Char List
al = ['a', 'd', 'e', 'c', 'b']
al.sort(reverse=True)
print('List in Descending Order: ', al)
al.sort()
print('List in Ascending Order: ', al)
# Sort String List
cities = ['Mumbai', 'London', 'Paris', 'New York']
cities.sort()
print('List in Ascending Order: ', cities)
cities.sort(reverse=True)
print('List in Descending Order: ', cities)
# Sort by String Length
cities = ['Mumbai', 'London', 'Paris', 'New York']
cities.sort(key=len)
print('List in Ascending Order of the length: ', cities)
cities.sort(key=len, reverse=True)
print('List in Descending Order of the length: ', cities)
# Sort List of Class Objects


class student:
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = student('Bill', 25)
s2 = student('Steve', 29)
s3 = student('Ravi', 26)
student_list = [s1, s2, s3]
# student_list.sort() # raise an error

student_list.sort(key=lambda s: s.name)  # sorts using lambda function

print('Students in Ascending Order:', end=' ')

for std in student_list:
    print(std.name, end=', ')

# sorts using lambda function
student_list.sort(key=lambda s: s.name, reverse=True)

print('Students in Descending Order:', end=' ')

for std in student_list:
    print(std.name, end=', ')
