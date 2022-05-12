# Finding in list
letters = ['a', 'b', 'c', 'd', 'e']

# print(letters.index("f"))  # Will show ValueError
if 'a' in letters:  # If want to overcome previous error
    print(letters.index("c"))
print(letters.count('g'))
print(letters.count('b'))
