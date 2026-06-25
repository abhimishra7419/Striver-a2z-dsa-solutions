'''My Brute force'''
# class Solution:
#     def count_reverse(self, arr):
#         n = len(arr)
#         count = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 if arr[i] > (2*arr[j]):
#                     count += 1
#         return count
# arr = [4, 1, 2, 3, 1]
# a = Solution()
# print(a.count_reverse(arr))

'''Optimal approach'''
class Solution:
    def merge(self, arr, low, mid, high):
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
    
    def count_pairs(self, arr, low, mid, high):
        count = 0
        right = mid + 1
        for i in range(low, mid+1):
            while right <= high and arr[i] > 2*arr[right]:
                right += 1
            count += (right - (mid+1))
        return count

    def merge_sorting(self, arr, low, high):
        count = 0
        if low >= high:
            return count
        mid = (low + high)//2
        count += self.merge_sorting(arr, low, mid)
        count += self.merge_sorting(arr, mid+1, high)
        count += self.count_pairs(arr, low, mid, high)
        self.merge(arr, low, mid, high)
        return count
    
    
    def count_reverse(self, arr):
        return self.merge_sorting(arr, 0, len(arr)-1)
    
arr = [4, 1, 2, 3, 1]
a = Solution()
print(a.count_reverse(arr))