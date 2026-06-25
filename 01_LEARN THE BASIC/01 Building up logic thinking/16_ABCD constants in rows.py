n = int(input("Enter number of row: "))
num = 0
for i in range(1, n+1):
    for j in range(i):
        print(chr(65+num), end="")
    print()
    num += 1
     