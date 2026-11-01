'''Optimal Solution'''
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = []

        # Total number of subsets is 2^n
        # 1 << n is equivalent to 2^n
        for i in range(1 << n):
            subset = []
            for j in range(n):
                # Check if the j-th bit of i is set to 1
                if (i >> j) & 1:
                    subset.append(nums[j])
            res.append(subset)

        return res
