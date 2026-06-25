'''My Brute froce'''
# class Solution:
#     def Merge_overlapping(self, arr):
#         n = len(arr)
#         arr.sort()
#         ans = []
#         e = 0
#         for i in range(n):
#             starting_limit = arr[i][0]
#             end_limit = arr[i][1]
#             if e >= i:
#                 continue
#             for j in range(i+1, n):
#                 if arr[j][0] <= end_limit:
#                     end_limit = max(end_limit, arr[j][1])
#                     e = j

#             ans.append([starting_limit, end_limit])
#         return ans
# arr = [[1,3], [2,6], [4, 7], [8,10],[15,18]]
# a = Solution()
# print(a.Merge_overlapping(arr))


'''Brute force'''
# class Solution:
#     def Merge_overlapping(self, arr):
#         n = len(arr)
#         arr.sort()
#         ans = []
#         i = 0
#         while i < n:
#             starting_limit = arr[i][0]
#             end_limit = arr[i][1]
#             j = i+1
#             while j < n and end_limit >= arr[j][0]:
#                 end_limit = max(end_limit, arr[j][1])
#                 j += 1
#             ans.append([starting_limit, end_limit])
#             i = j
#         return ans
# arr = [[1,3], [2,6], [4, 7], [8,10],[15,18]]
# a = Solution()
# print(a.Merge_overlapping(arr))


'''Optimal approach'''
class Solution:
    def Merge_overlapping(self, arr):
        n = len(arr)
        arr.sort()
        ans = []
        for i in range(n):
            if not ans or ans[-1][1] < arr[i][0]:
                ans.append([arr[i][0], arr[i][1]])
            else: 
                ans[-1][1] = max(ans[-1][1], arr[i][1])
        return ans
arr = [[1,3], [2,6], [4, 7], [8,10], [15,18]]
a = Solution()
print(a.Merge_overlapping(arr))