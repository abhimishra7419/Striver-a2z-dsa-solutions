class solution:
    def marge(self, arr, low, mid, high):
        temp = []
        left, right = low, mid+1
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1
        for i in range(low, high+1):
            arr[i] = temp[i - low]

    def margesort(self, arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        self.margesort(arr, low, mid)
        self.margesort(arr, mid+1, high)
        self.marge(arr, low , mid, high)
arr = [5, 2, 8, 4, 1]
a = solution()
a.margesort(arr, 0, len(arr)-1)
print(arr)