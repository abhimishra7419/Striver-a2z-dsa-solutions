'''Brute force'''
# class Solution:
#     def singleNumber(slef, nums):
#         mpp = {}
#         ans = []
#         for num in nums:
#             mpp[num] = mpp.get(num, 0)+1
#         for value, key in mpp.items():
#             if key == 1:
#                 ans.append(value)
#         return ans
# arr =  [-1, 0]
# a = Solution()
# print(a.singleNumber(arr))

'''Optimal approach'''
class Solution:
    def singleNumber(self, nums):
        xor = 0

        for num in nums:
            xor ^= num

        bit = xor & -xor   # or bit = (xor & (xor-1))^xor

        num1 = 0
        num2 = 0

        for num in nums:
            if num & bit:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]
arr =  [-1, 0]
a = Solution()
print(a.singleNumber(arr))