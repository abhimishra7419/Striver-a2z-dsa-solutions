# class solution:
#     def reverse(self, n):
#         v = n
#         rev = 0
#         while v > 0:
#             lastdigit = v % 10
#             rev = rev*10 + lastdigit
#             v //= 10
#         if rev == n:
#             return "Palindrome Number"
#         else:
#             return "Not Palindrome"
# a = solution()
# print(a.reverse(11))
# print(a.reverse(1111))
# print(a.reverse(4554))


class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = 0
        n = x
        while n > 0:
            lastdigit = n % 10
            y = y*10 + lastdigit
            n //= 10
        if y == x:
            return True
        return False
a = Solution()
print(a.isPalindrome(121))
print(a.isPalindrome(1111))