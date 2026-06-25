class solution:
    def factorial(self, n):
        num = 1
        for i in range(2, n+1):
            num *= i
        return num
a = solution()
print(a.factorial(5))