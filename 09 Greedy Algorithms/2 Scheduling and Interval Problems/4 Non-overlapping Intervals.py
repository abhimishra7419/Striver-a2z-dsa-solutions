'''Optimal Solution'''
class Solution:
    def eraseOverlapIntervals(self, intervals):
        # Sort intervals by their end time in ascending order
        intervals.sort(key=lambda x: x[1])
        
        removals = 0
        prev_end = float('-inf')
        
        for start, end in intervals:
            if start >= prev_end:
                # No overlap; keep this interval and update the boundary
                prev_end = end
            else:
                # Overlap detected; discard the current interval
                removals += 1
                
        return removals
a = Solution()
Intervals = [ [1, 2] , [2, 3] , [3, 4] ,[1, 3] ]
print(a.eraseOverlapIntervals(Intervals))