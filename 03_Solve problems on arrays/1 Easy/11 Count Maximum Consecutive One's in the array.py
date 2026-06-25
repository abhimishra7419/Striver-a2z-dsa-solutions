class Solution:
    def count_max(self, arr):
        n = len(arr)
        count = 0
        m = 0
        for i in range(n):
            if arr[i] == 1:
                count += 1
            else:
                count = 0
            m = max(m, count)
        return f"Maximum number of in consecutive 1's is {m}"
arr = [0, 1, 1, 1, 1, 0, 0, 0, 1]
a = Solution()
print(a.count_max(arr))