n = int(input("Enter number of rows you went: "))
# i = 1
# j = 1 
# k = 1
# while (i<=n):
#     while(j<=(i+k-1)):
#         print(f"{j} ", end="")
#         j+=1
#     k=j
#     print()
#     i+=1


# More ↓ easy and simple code
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(f"{num} ", end="")
        num += 1
    print()