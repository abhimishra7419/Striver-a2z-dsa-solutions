'''My brute force'''
# class Solution:
#     def finding_single(self, arr):
#         n = len(arr)
#         mpp = {}
#         for i in range(n):
#             mpp[arr[i]] = mpp.get(arr[i], 0) + 1
#         for key, value in mpp.items():
#             if value == 1:
#                 return key
#         return 0
# arr = [1,1,2,2,3,3,4,5,5,6,6]
# a = Solution()
# print(a.finding_single(arr))

'''Better approach - I'''
# class Solution:
#     def finding_single(self, arr):
#         n = len(arr)
#         if n == 1:
#             return arr[0]
#         for i in range(n):
#             if i == 0:
#                 if arr[i] != arr[i+1]:
#                     return arr[i]
#             elif i == n-1:
#                 if arr[i] != arr[i-1]:
#                     return arr[i]
#             else:
#                 if arr[i] != arr[i+1] and arr[i] != arr[i-1]:
#                     return arr[i]
#         return -1
# arr = [1,1,2,2,3,3,4,5,5,6,6]
# a = Solution()
# print(a.finding_single(arr))


'''Better approach - II'''
# class Solution:
#     def finding_single(self, arr):
#         n = len(arr)
#         xor = 0
#         for i in range(n):
#             xor ^= arr[i]
#         return xor
# arr = [1,1,2,2,3,3,4,5,5,6,6]
# a = Solution()
# print(a.finding_single(arr))

'''Optimal approach'''
class Solution:
    def finding_single(self, arr):
        n = len(arr) - 1
        if n == 0:
            return arr[n]
        if arr[0] != arr[1]:
            return arr[0]
        if arr[n] != arr[n-1]:
            return arr[n]
        
        low = 1
        high = n
        while low <= high:
            mid = low + high //2
            if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
                return arr[mid]
            if  (mid % 2 == 1 and arr[mid] == arr[mid-1]) or \
                (mid % 2 == 0 and arr[mid] == arr[mid+1]):
                low = mid + 1
            else:
                high = mid - 1
        return -1
arr = [3,3,7,7,10,11,11]
a = Solution()
print(a.finding_single(arr))
