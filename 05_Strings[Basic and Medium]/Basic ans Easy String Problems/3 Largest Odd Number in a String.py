'''My approach'''
# class Solution:
#     def findingLargestOdd(self, s):
#         value = int(s)
#         max_value = float('-inf')
#         for _ in range(len(s)):
#             if value % 2 == 1 or value % 2 == -1:
#                 if value > max_value:
#                     max_value = value
#             if value < 0:
#                     value = (-1 * value) // 10
#                     value = -1 * value
#             else:
#                 value //= 10
#         if max_value == float('-inf'):
#              max_value = -1
#         return str(max_value)
# s = "-0214638"
# a = Solution()
# print(a.findingLargestOdd(s))

'''apporach'''
# class Solution:
#     def findingLargestOdd(self, s):
#         ind = -1
#         for i in range(len(s)-1 , -1, -1):
#             if (int(s[i])%2) == 1:
#                 ind = i
#                 break
#         i = 0
#         while i <= ind and s[i] == '0':
#             i += 1
#         return s[i:ind+1]
# s = "0214638"
# a = Solution()
# print(a.findingLargestOdd(s))


'''Optimal aproach'''
class Solution:
    def findingLargestOdd(self, s):
        for i in range(len(s)-1, -1, -1):
            if s[i] in "13579":
                return s[:i+1]
        return ""
s = "0214638"
a = Solution()
print(a.findingLargestOdd(s))