class Solution:
    def Rbubble(self, arr, n):
        if n == 1:
            return
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        self.Rbubble(arr, n-1)

arr = [3, 5, 2, 1, 5, 3, 6]
a = Solution()
a.Rbubble(arr, len(arr))
print(arr)