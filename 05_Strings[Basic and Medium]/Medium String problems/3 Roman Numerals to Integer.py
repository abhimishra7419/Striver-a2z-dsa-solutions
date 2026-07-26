'''My apporach'''
class Solution:
    def ConvertingfromRoman(self, s):
        mpp = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        total_val = 0
        for i in range(len(s)-1):
            if mpp[s[i]] < mpp[s[i+1]]:
                total_val -= mpp[s[i]]
            else:
                total_val += mpp[s[i]]
        return total_val+mpp[s[-1]]
s = "MCMXCIV"
a = Solution()
print(a.ConvertingfromRoman(s))