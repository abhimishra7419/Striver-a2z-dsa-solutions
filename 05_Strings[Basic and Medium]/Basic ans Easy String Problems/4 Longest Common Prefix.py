'''approach'''
class Solution:
    def LongestCommonPrefix(self, str):
        if not str:
            return ""
        str.sort()
        first = str[0]
        last = str[-1]
        ans = []
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return "".join(ans)
            ans.append(first[i])
        return "".join(ans)
strs = ["flower","flow","flight"]
a = Solution()
print(a.LongestCommonPrefix(strs))