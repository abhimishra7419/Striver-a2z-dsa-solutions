class solution:
    def insertion_sort(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i-1
            while (j >= 0) and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr
a = solution()
print(a.insertion_sort([1, 2, 5, 3, 2, 1, 5, 7, 4, 3, 2]))