v = int(input())
w = int(input())

if ((w % 2) != 0) or w < 2 or w <= v:
    print("INVALID INPUT")
else:
    x = ((4*v)-w)//2
    print(f'TW = {x} FW = {v-x}')
