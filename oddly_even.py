n = (input())
e = 0
o = 0
for i in range(0, len(n)):
    if i % 2 == 0:
        e += int(n[i])
    else:
        o += int(n[i])
print(abs(e-o))
