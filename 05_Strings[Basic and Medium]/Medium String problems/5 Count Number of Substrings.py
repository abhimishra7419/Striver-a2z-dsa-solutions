'''approach'''
class Solution:
    def AtMostKDistinct(self, s, k):
        freq = {}
        left, res = 0, 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0)+1

            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            res += (right - left + 1)
        return res
    def NumberofSubString(self, s, k):
        return self.AtMostKDistinct(s, k) - self.AtMostKDistinct(s, k-1)
s = "abcbaa"
k = 3  
a = Solution()
print(a.NumberofSubString(s, k))
