'''approach'''
class Solution:
    def countingBitFlips(self, start, goal):
        n = start ^ goal
        count = 0
        while n > 0:
            n = n & (n-1)
            count += 1
        return count
if __name__ == "__main__":
    start = 10
    goal = 7
    a = Solution()
    print(a.countingBitFlips(start, goal))