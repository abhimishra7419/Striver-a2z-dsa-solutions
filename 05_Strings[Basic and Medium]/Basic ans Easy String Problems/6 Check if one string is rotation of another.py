'''My Brute force'''
# class Solution:
#     def checkingString(self, s, goal):
#         if len(s) != len(goal):
#             return False
#         for _ in range(len(s)):
#             if s == goal:
#                 return True
#             val = s[0]
#             s = s[1:]
#             s += val
#         return False
# s = "rotation"
# goal = "tionrota"
# a = Solution()
# print(a.checkingString(s, goal))


'''My brute force-II'''
# class Solution:
#     def checkingString(self, s, goal):
#         if len(s) != len(goal):
#             return False
#         m = list(s)
#         m2 = list(goal)
#         for i in range(len(s)):
#             if m == m2:
#                 return True
#             val = m[0]
#             m.pop(0)
#             m.append(val)
#         return False
# s = "rotation"
# goal = "tionrota"
# a = Solution()
# print(a.checkingString(s, goal))

'''optimal approach'''
class Solution:
    def checkingString(self, s, goal):
        if len(s) != len(goal):
            return False
        double_s = s+s
        return goal in double_s
s = "rotation"
goal = "tionrota"
a = Solution()
print(a.checkingString(s, goal))
