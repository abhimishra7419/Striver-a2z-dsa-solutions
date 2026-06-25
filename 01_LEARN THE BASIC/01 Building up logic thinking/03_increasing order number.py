n = int(input("Enter your number that you need to pattern should print: "))
i = 1
while(i <= n):            # rows
    j = 1                 # reseting value 
    while(j <= i):        # column
        print(j, end="") 
        j += 1
    print()
    i += 1