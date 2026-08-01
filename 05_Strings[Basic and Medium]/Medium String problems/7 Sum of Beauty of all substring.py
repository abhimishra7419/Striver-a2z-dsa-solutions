'''My approach'''
class Solution:
    def beautyofSubstring(self, s):
        n = len(s)
        total_beauty = 0
        for i in range(n):
            freq = {}
            for j in range(i, n):
                freq[s[j]] = freq.get(s[j], 0) + 1
                values = freq.values()
                max_v = max(values)
                min_v = min(values)
                total_beauty += (max_v - min_v)
        return total_beauty
s = "aabcbaa"
a = Solution()
print(a.beautyofSubstring(s))