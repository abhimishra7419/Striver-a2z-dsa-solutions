class solution:
    def armstrong(self, n):
        Noofdigits = len(str(n))
        x = n
        y = 0
        while x > 0:
            lastdigit = x % 10
            y = y + lastdigit ** Noofdigits
            x //= 10
        if y == n:
            return True
        else:
            return False
a = solution()
print(a.armstrong(153))
print(a.armstrong(371))
print(a.armstrong(157))