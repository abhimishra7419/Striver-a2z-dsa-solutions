n = int(input("Enter your number that you need to pattern should print: "))
i = n
while(i >= 0):
    j = 1
    while(j  <= i):
        print(j, end="") 
        j += 1
    print()
    i -= 1