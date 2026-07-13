'''My brute force'''
# class Solution:
#     def subarry(self, arr, k):
#         n = len(arr)
#         count = 0
#         for i in range(n):
#             Xor = 0
#             for j in range(i, n):
#                 Xor ^= arr[j]
#                 if Xor == k:
#                     count += 1
#         return count
# arr = [4, 2, 2, 6, 4]
# k = 6
# a = Solution()
# print(a.subarry(arr, k))

'''Optimal approach'''
class Solution:
    def subarry(self, arr, k):
        n = len(arr)
        mpp = {0:1}
        Xor = 0
        count = 0
        for i in range(n):
            Xor ^= arr[i]
            requried = Xor ^ k
            if requried in mpp:
                count += mpp[requried]
            
            mpp[Xor] = mpp.get(Xor, 0)+1
        return count
arr = [4, 2, 2, 6, 4]
k = 6
a = Solution()
print(a.subarry(arr, k))