'''My approach'''  # space complexity:- O(N)
# class Solution:
#     def removingParentheses(self, s):
#         result = []
#         stack = []
#         for char in s:
#             if char == '(':
#                 if len(stack) > 0:
#                     result.append('(')
#                 stack.append(char)
#             if char == ')':
#                 stack.pop()
#                 if len(stack) > 0:
#                     result.append(char)
#         return "".join(result)
# s = "()(()())(())"
# a = Solution()
# print(a.removingParentheses(s))




'''Approach'''
class Solution:
    def removingParentheses(self, s):
        result = ""
        level = 0
        for char in s:
            if char == '(':   # "(" and '('  are same in python
                if level > 0:
                    result += char
                level += 1

            elif char == ")":
                level -= 1
                if level > 0:
                    result += char
        return result
s = "()(()())(())"
a = Solution()
print(a.removingParentheses(s))