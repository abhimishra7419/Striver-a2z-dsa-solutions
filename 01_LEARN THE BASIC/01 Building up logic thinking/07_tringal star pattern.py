'''n = int(input("Enter you tringal lenth: "))
for i in range(1, n+1):
    print(" "*(n-i), end= "")
    print("*"*(2*i - 1), end="")
    print(" "*(n-i)) '''

# ↓ improve version

n = int(input("Enter you tringal lenth: "))
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i - 1))