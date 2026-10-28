'''My brute force'''
# class Solution:
#     def singleNumber(self, arr):
#         mpp = {}
#         for i in range(len(arr)):
#             mpp[arr[i]] = mpp.get(arr[i], 0)+1
#         for key, value in mpp.items():
#             if value == 1:
#                 return key
#         return -1
# if __name__ == "__main__":
#     arr = [2, 2, 2, 3]
#     a = Solution()
#     print(a.singleNumber(arr))


'''Optimal approach'''
class Solution:
    def singleNumber(self, nums):
        ones = 0
        twos = 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones

if __name__ == "__main__":
    arr = [1, 0, 3, 10, 1, 1, 3, 3, 10, 10]
    a = Solution()
    print(a.singleNumber(arr))
