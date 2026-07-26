'''My approach'''
class Solution:
    def MaximumNestingCount(self, s):
        nesting = 0
        max_nesting = 0
        for chr in s:
            if chr == '(':
                nesting += 1
                max_nesting = max(max_nesting, nesting)
            elif chr == ')':
                nesting -= 1
        return max_nesting
s = "(1+(2*3)+((8)/4))+1"
a = Solution()
print(a.MaximumNestingCount(s))