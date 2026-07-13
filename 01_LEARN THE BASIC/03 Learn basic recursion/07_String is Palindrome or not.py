# class solution():
#     def palindrome(self, s):
#         p1 = 0
#         p2 = len(s)-1
#         while p1 < p2:
#             if s[p1] != s[p2]:
#                 return "Not Palindrome"
#             p1 += 1
#             p2 -= 1
#         return "Palindrome"
# a = solution()
# print(a.palindrome("ABCDDCBA"))
# print(a.palindrome("ABHI"))
# print(a.palindrome("ABCDCBA"))
# print(a.palindrome("TAKE U FORWARD"))

# very basic code 
# ↓ advance code

class Solution():
    def palindrome(self, s):
        left, right = 0, len(s)-1
        while left < right:
            if not s[left].isalnum():  # If that particular chareter is not letter or number skip it.
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
a = Solution()
print(a.palindrome("ABCDDCBA"))
print(a.palindrome("ABHI"))
print(a.palindrome("ABCDCBA"))
print(a.palindrome("A man, a plan, a canal: panama"))