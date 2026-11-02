'''Optimal Solution'''
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Swap characters using Python's tuple unpacking
            s[left], s[right] = s[right], s[left]
            
            # Move pointers closer to the center
            left += 1
            right -= 1
a = Solution()
s = ["h", "e" ,"l" ,"l" ,"o"]
a.reverseString(s)
print(s)