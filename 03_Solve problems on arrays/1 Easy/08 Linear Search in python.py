class Solution:
    def search(self, arr, num):
        for i in range(len(arr)):
            if arr[i] == num:
                return f"The index of {num} is {i}"
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = Solution()
print(a.search(arr, 10))