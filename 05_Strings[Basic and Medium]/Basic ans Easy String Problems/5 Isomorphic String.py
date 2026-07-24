'''My brute approach'''
# class Solution:
#     def Isomorphic(self, s, t):
#         if len(s) != len(t):
#             return False
#         mpp = {}
#         reversed_mpp = {}
#         for i in range(len(s)):
#             if s[i] in mpp:
#                     if mpp[s[i]] != t[i]:
#                         return False
#             if t[i] in reversed_mpp:
#                 if reversed_mpp[t[i]] != s[i]:
#                     return False
#             mpp[s[i]] = t[i]
#             reversed_mpp[t[i]] = s[i]
#         return True
# s = "far"
# t = "aar"
# a = Solution()
# print(a.Isomorphic(s, t))


'''My Optimal apporach'''
# class Solution:
#     def Isomorphic(self, s, t):
#         if len(s) != len(t):
#             return False
#         freq, rev_freq = [0]*256, [0]*256     # freq, rev_freq are using as mapping
#         for i in range(len(s)):
#             asc_s = ord(s[i])
#             asc_t = ord(t[i])
#             if freq[asc_s] != asc_t and freq[asc_s] != 0:
#                 return False
#             if rev_freq[asc_t] != asc_s and rev_freq[asc_t] != 0:
#                 return False
#             if freq[asc_s] == 0:
#                 freq[asc_s] = asc_t
#             if rev_freq[asc_t] == 0:
#                 rev_freq[asc_t] = asc_s
#         return True
# s = "paper"
# t = "title"
# a = Solution()
# print(a.Isomorphic(s, t))



'''Optimal approach'''
class Solution:
    def Isomorphic(self, s, t):
        if len(s) != len(t):
            return False
        m1, m2 = [0]*256, [0]*256
        for i in range(len(s)):
            if m1[ord(s[i])] != m2[ord(t[i])]:
                return False
            m1[ord(s[i])] = i+1   # its store last seen of character,
            m2[ord(t[i])] = i+1 
        return True
s = "paa"
t = "tti"
a = Solution()
print(a.Isomorphic(s, t))
