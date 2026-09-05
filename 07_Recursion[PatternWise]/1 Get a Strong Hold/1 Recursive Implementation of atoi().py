'''My approach'''
class Solution:
    def helper(self, s, i, num, sign):
        INT_min = -2**31
        INT_max = 2**31 -1
        if i >= len(s) or not s[i].isdigit():
            return sign*num
        num = num*10 + int(s[i])
        if sign*num <= INT_min: return INT_min
        if sign*num >= INT_max: return INT_max
        return self.helper(s, i+1, num, sign)
    def MyAtoi(self, s):
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        sign = 1
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        return self.helper(s, i, 0, sign)
if __name__ == "__main__":
    s = " "
    a = Solution()
    print(a.MyAtoi(s))  # Output: -12345