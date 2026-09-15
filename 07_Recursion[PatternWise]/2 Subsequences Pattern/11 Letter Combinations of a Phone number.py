'''approach'''
class Solution:
    def __init__(self):
        self.map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    def helper(self, digits, ans, index, current):
        if index == len(digits):
            ans.append(current)
            return
        s = self.map[int(digits[index])]
        for char in s:
            self.helper(digits, ans, index + 1, current + char)
    def letterCombinations(self, digits):
        ans = []
        if not digits:
            return ans
        self.helper(digits, ans, 0, "")
        return ans
if __name__ == "__main__":
    solution = Solution()
    digits = "23"
    result = solution.letterCombinations(digits)
    print(result)