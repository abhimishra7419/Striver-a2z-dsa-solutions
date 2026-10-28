'''Optimal approach'''
class Solution:
    def singleNumber(self, nums):
        xor = 0

        # Step 1: XOR all elements
        for num in nums:
            xor ^= num

        # Step 2: Find the rightmost set bit
        bit = xor & -xor

        num1 = 0
        num2 = 0

        # Step 3: Divide numbers into two groups
        for num in nums:
            if num & bit:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]
arr =  [-1, 0]
a = Solution()
print(a.singleNumber(arr))