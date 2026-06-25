'''My approach'''
# class Solution:
#     def count_subarry(self, arr, k):
#         n = len(arr)
#         count = 0
#         for i in range(n):
#             sum = 0
#             for j in range(i, n):
#                 # if sum+arr[j] <= k:
#                 sum += arr[j]
#                 if sum == k:
#                     count += 1
#         return count
# arr = [3, 1, 2, 4] 
# a = Solution()
# print(a.count_subarry(arr, 6))

# '''Optimal approach'''
class Solution:
    def count_subarry(self, arr, k):
        n = len(arr)
        prefixsumcount = {}
        prefixsum = 0
        count = 0
        prefixsumcount[0] = 1
        for i in range(n):
            prefixsum += arr[i]
            remove = prefixsum - k
            if remove in prefixsumcount:
                count += prefixsumcount[remove]
            prefixsumcount[prefixsum] = prefixsumcount.get(prefixsum, 0) + 1
        return count
arr = [1, 2, 1] 
a = Solution()
print(a.count_subarry(arr, 3))