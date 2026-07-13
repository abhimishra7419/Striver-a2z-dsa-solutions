class Solution:
    def Left_Rotate(self, arr):
        key = arr[0]
        k = 0
        n = len(arr)
        for i in range(1, n):
            arr[k] = arr[i]
            k += 1
        arr[n - 1] = key
arr = [1, 2, 3, 4, 5]
a = Solution()
a.Left_Rotate(arr)
print(arr)