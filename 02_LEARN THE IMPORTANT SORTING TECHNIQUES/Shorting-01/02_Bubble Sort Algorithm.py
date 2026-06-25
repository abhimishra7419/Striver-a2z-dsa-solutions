class solution:
    def bubble_sorting(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(n-1):
                if arr[j+1] < arr[j]:   # compearing with neighors
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
a = solution()
print(a.bubble_sorting([1, 3, 5, 7, 3, 5, 7, 8, 9, 3, 6, 7]))