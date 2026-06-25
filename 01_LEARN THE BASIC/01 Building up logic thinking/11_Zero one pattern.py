'''n = int(input("Enter lenth of pettern: "))
for i in range(1, n+1):
    for k in range(1, i+1):
        if ((i+k)%2 == 0):
            print("1", end="")
        if ((i+k)%2 != 0):
            print("0", end="")
    print()'''


# ↓ improved version

n = int(input("Enter lenth of pettern: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        if ((i+j)%2 == 0):
            print("1", end="")
        else:
            print("0", end="")
    print()