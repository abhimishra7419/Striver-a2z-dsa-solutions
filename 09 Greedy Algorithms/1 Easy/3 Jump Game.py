'''Optimal Solution'''
class Solution:
    def canJump(self, nums):
        max_reach = 0
        
        for i, jump in enumerate(nums):
            # If the current index is beyond the farthest reachable point, we are stuck
            if i > max_reach:
                return False
            
            # Update the farthest index we can reach from the current position
            max_reach = max(max_reach, i + jump)
            
            # Early exit if we can already reach or pass the last index
            if max_reach >= len(nums) - 1:
                return True
                
        return True
a = Solution()
nums = [2,3,1,1,4]
print(a.canJump(nums))