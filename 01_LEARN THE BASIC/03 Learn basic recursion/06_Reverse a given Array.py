class solution:
    def reverse(self , arr):
        p1 = 0
        p2 = len(arr)-1
        while p1 < p2:
            arr[p1], arr[p2] = arr[p2], arr[p1]
            p1 += 1
            p2 -= 1
        return arr
a = solution()
print(a.reverse([1, 2, 3, 4, 5]))