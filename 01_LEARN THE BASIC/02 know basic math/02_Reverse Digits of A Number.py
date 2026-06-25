class solution:
    def reverse(self, n):
        rev = 0
        sing = 1
        if n < 0:
            n = -1 * n
            sing = -1
        while n > 0:
            lastdigit = n % 10
            rev = rev*10 + lastdigit
            n //= 10
        if rev < (-2**31) or rev > (2**31-1):
            return 0
        return rev*sing
a = solution()
print(a.reverse(-123))