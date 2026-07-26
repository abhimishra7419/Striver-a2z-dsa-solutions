'''My approach'''
# class Solution:
#     def sorting(self, s):
#         n = len(s)
#         mpp = {}
#         m = []
#         for i in range(n):
#             mpp[s[i]] = mpp.get(s[i], 0)+1
#         sorted_mpp = dict(sorted(mpp.items(), key=lambda item: item[1], reverse=True))
#         val = 0
#         for key, value in sorted_mpp.items():
#             if val == 0:
#                 val = value
#                 k = key
#                 continue
#             if val == sorted_mpp[key]:
#                 if ord(k) < ord(key):
#                     for i in range(val):
#                         m.append(k)
#                     val = value
#                     k = key
#                 else:
#                     for i in range(value):
#                         m.append(key)
#             else:
#                 for i in range(val):
#                     m.append(k)
#                 val = value
#                 k = key
#         for i in range(val):
#             m.append(k)
#         return "".join(m)
# s = "aaaajjrr"
# a = Solution()
# print(a.sorting(s))




'''My approach'''# changes for leetcode
class Solution:
    def sorting(self, s):
        n = len(s)
        mpp = {}
        m = []
        for i in range(n):
            mpp[s[i]] = mpp.get(s[i], 0)+1
        sorted_mpp = dict(sorted(mpp.items(), key=lambda item: item[1], reverse=True))
        return "".join(key*value for key, value in sorted_mpp.items())
s = "aaaajjrr"
a = Solution()
print(a.sorting(s))



"""simple approach"""
# from collections import Counter
# class Solution:
#     def sorting(self, s):
#         return "".join([alpha*k for alpha, k in Counter(s).most_common()])
# s = "aaaajjrr"
# a = Solution()
# print(a.sorting(s))
