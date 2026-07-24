'''My brute force'''
# class Solution:
#     def anagramsString(self, s, t):
#         if len(s) != len(t):
#             return False
#         if sorted(s) == sorted(t):
#             return True
#         return False
# s, t = "CAT", "ACT"
# a = Solution()
# print(a.anagramsString(s, t))


'''My optimal approach'''
class Solution:
    def anagramsString(self, s, t):
        if len(s) != len(t):
            return False
        m1 = [0]*256
        m2 = [0]*256
        for i in range(len(s)):
            m1[ord(s[i])] += 1
            m2[ord(t[i])] += 1
        return m1 == m2
s, t = "CAT", "ACT"
a = Solution()
print(a.anagramsString(s, t))
