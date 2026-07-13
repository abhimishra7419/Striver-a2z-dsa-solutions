'''brute force'''
# class Solution:
#     def calculatingPages(self, arr, pages):
#         sum = 0
#         students = 1
#         n = len(arr)
#         for i in range(n):
#             if sum + arr[i] <= pages:
#                 sum += arr[i]
#             else:
#                 students += 1
#                 sum = arr[i]
#         return students
#     def allocation(self, arr, students):
#         low = max(arr)
#         high = sum(arr)
#         if students > len(arr):
#             return -1
#         for pages in range(low, high+1):
#             if self.calculatingPages(arr, pages) == students:
#                 return pages
#         return low
# arr = [12, 34, 67, 90]
# m = 2
# a = Solution()
# print(a.allocation(arr, m))



'''My Optimal approach'''
class Solution:
    def calculating(self, arr, mid):
        sum = 0
        students = 1
        for i in range(len(arr)):
            if sum + arr[i] <= mid:
                sum += arr[i]
            else:
                students += 1
                sum = arr[i]
        return students
    def allocation(self, arr, students):
        low = max(arr)
        high = sum(arr)
        ans = low
        if students > len(arr):
            return -1
        while low <= high:
            mid = (low + high)//2
            mycalculatedstudent = self.calculating(arr, mid)
            if mycalculatedstudent <= students:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
arr = [12, 34, 67, 90]
m = 2
a = Solution()
print(a.allocation(arr, m))
