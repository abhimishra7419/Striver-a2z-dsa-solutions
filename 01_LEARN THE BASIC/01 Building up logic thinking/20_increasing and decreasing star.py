n = int(input("Enter you pattern lenth: "))
x = int(n//2)
for i in range(x-1, -1, -1):
    print("*"*(x-i) + " "*(2*i) + "*"*(x-i))
for i in range(1, x):
    print("*"*(x-i) + " "*(2*i) + "*"*(x-i))