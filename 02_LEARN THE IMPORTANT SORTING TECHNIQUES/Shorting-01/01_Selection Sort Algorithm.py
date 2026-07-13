class solution:
    def sorting(self, arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:  # one element compare to all
                    min_index = j
                    arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
a = solution()
print(a.sorting([3, 5, 6, 7, 2, 1, 5, 6]))