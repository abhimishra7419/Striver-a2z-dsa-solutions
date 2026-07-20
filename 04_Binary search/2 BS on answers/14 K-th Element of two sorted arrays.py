'''approach'''
class Solution:
    def finidingkthelement(self, arr1, arr2, k):
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1
        n1, n2 = len(arr1), len(arr2)
        left = k
        low, high = max(0, k-n2), min(k, n1)
        while low <= high:
            mid1 = (low + high) >> 1   # same as (low + high)//2
            mid2 = left - mid1
            l1 = arr1[mid1-1] if mid1 > 0 else float('-inf')
            l2 = arr2[mid2-1] if mid2 > 0 else float('-inf')
            r1 = arr1[mid1] if mid1 < n1 else float('inf')
            r2 = arr2[mid2] if mid2 < n2 else float('inf')
            if l2 <= r1 and l1 <= r2:
                return max(l1, l2)
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return -1
arr1 = [100, 112, 256, 349, 770]
arr2 = [72, 86, 113, 119, 265, 445, 892]
k = 7
a = Solution()
print(a.finidingkthelement(arr1, arr2, k))