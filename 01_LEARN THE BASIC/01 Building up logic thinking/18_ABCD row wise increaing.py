n = int(input("Entr the number of row: "))
for k in range(1, n+1):
    num = n-k
    for i in range(k):
        print(chr(65+num), end="")
        num += 1
    print()