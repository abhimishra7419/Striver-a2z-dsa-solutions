'''Optimal approach-I''' # Without recursion
# class Solution:
#     def getSubsequences(self, s):
#         n = len(s)
#         total = 1 << n
#         subsequences = []
#         for mask in range(total):
#             subseq = []
#             for i in range(n):
#                 if mask & (1 << i):
#                     subseq.append(s[i])
#             subsequences.append("".join(subseq))
#         return subsequences

# if __name__ == "__main__":
#     s = "abc"
#     sol = Solution()
#     print(sol.getSubsequences(s))


'''Opitimal approach-II'''
class Solution:
    def helper(self, s, index, current, result):
        if index == len(s):
            result.append("".join(current))
            return
        self.helper(s, index + 1, current, result)
        current.append(s[index])
        self.helper(s, index + 1, current, result)
        current.pop()
    def getSubsequences(self, s):
        result = []
        current = []
        self.helper(s, 0, current, result)
        return result

if __name__ == "__main__":
    s = "abc"
    sol = Solution()
    print(sol.getSubsequences(s))