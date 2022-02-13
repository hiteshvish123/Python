N = int(input())
if not 1 <= N <= 1000:
    print("Invalid Input")

H = [str(N)]
for I in range(0, len(str(N))):
    H[I] = input()
    if 1 <= int(H[I]) <= 100000:
        print("Enter value of K: ")
    else:
        print("Invalid Input")
        break

K = int(input())
if not 1 <= K <= N:
    print("Invalid Input")
