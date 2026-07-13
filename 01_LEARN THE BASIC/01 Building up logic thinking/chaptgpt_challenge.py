n = int(input("Enter your number that you need to pattern should print: "))
i = 1
while(i <= n):
    j = 0
    while(j < i):
        print(i-j, end="") 
        j += 1
    print()
    i += 1