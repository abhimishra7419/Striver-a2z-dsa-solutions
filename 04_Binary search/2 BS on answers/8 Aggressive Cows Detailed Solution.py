'''My brute force'''
# class Solution:
#     def isposibile(self, arr, distance, k):
#         cover = arr[0]
#         k -= 1
#         for i in range(1, len(arr)):
#             if arr[i] >= cover + distance:
#                 k -= 1
#                 cover = arr[i]
#             if k == 0:
#                 return True
#         return False

#     def AggresiveCows(self, arr, k):
#         arr.sort()
#         low = 0
#         high = arr[-1] - arr[0]
#         for i in range(high, low, -1):
#             if self.isposibile(arr, i, k):
#                 return i
#         return -1
# arr = [4,2,1,3,6]
# k = 2
# a = Solution()
# print(a.AggresiveCows(arr, k))


'''My Optimal Solution'''
class Solution:
    def ispossibile(self, arr, distance, k):
        cover = arr[0]
        k -= 1
        for i in range(1, len(arr)):
            if arr[i] >= cover + distance:
                k -= 1
                cover = arr[i]
            if k == 0:
                return True
        return False
    def AggresiveCows(self, arr, k):
        arr.sort()
        low = 1
        high = arr[-1] - arr[0]
        ans = -1
        while low <= high:
            mid = (low + high)//2
            if self.ispossibile(arr, mid, k):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
arr = [0,3,4,7,10,9]
k = 4
a = Solution()
print(a.AggresiveCows(arr, k))