n = int(input("Enter rows number: "))
for i in range(1, n+1):
    print(" "*(n-i),end="")
    for k in range(i):
        print(chr(65+k),end= "")
    for j in range(i-1 , 0, -1):
        print(chr((65+k)-j),end= "")
    print()