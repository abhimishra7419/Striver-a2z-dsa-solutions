class solution:
    def sum(self, n):
        num = 0
        for i in range(n+1):
            num += i
        return num
a = solution()
print(a.sum(5))