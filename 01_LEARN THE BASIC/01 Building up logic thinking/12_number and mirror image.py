n = int(input("Enter your number: "))
for i in range(1, n+1):
    for k in range(1, i+1):
        print(k, end="")
    print(" "*(2*n-(2*i)), end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print()

# ↓ small improvment

# n = int(input("Enter your number: "))
# for i in range(1, n+1):
#     for k in range(1, i+1):
#         print(k, end="")
#     print(" "*(2*(n-i)), end="")
#     for j in range(i, 0, -1):
#         print(j, end="")
#     print()
