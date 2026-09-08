'''Brute force'''
# class Solution:
#     def is_valid(self, s):
#         balance = 0
#         for c in s:
#             if c == '(':
#                 balance += 1
#             else:
#                 balance -= 1
#             if balance < 0:
#                 return False
#         return balance == 0
#     def generate_all(self, curr, n, res):
#         if len(curr) == 2 * n:
#             if self.is_valid(curr):
#                 res.append(curr)
#             return
#         self.generate_all(curr + '(', n, res)
#         self.generate_all(curr + ')', n, res)
#     def generate_parenthesis(self, n):
#         res = []
#         self.generate_all("", n, res)
#         return res
# if __name__ == "__main__":
#     n = 3
#     a = Solution()
#     print(a.generate_parenthesis(n))

'''Optimal approach'''
class Solution:
    def backtrack(self, curr, open, close, n, res):
        if len(curr) == 2 * n:
            res.append(curr)
            return
        if open < n:
            self.backtrack(curr + '(', open + 1, close, n, res)
        if close < open:
            self.backtrack(curr + ')', open, close + 1, n, res)

    def generate_parenthesis(self, n):
        res = []
        self.backtrack("", 0, 0, n, res)
        return res

    
if __name__ == "__main__":
    n = 3
    a = Solution()
    print(a.generate_parenthesis(n))