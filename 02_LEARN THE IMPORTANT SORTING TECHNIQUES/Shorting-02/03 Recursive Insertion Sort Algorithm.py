class Solution:
    def Rinsertion(self, arr, i, n):
        if n == i:
            return
        j = i
        while j >= 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        self.Rinsertion(arr, i+1, n)
arr = [1, 2, 5, 3, 2, 1, 5, 7, 4, 3, 2]
n = len(arr)
a = Solution()
a.Rinsertion(arr, 0, n)
print(arr)