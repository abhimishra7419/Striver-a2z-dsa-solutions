'''My brute force'''
# class Solution:
#     def count_inversions(self, arr):
#         n = len(arr)
#         mid = n // 2
#         count = 0
#         for i in range(n):
#             for j in range(n):
#                 if i < j:
#                     if arr[i] > arr[j]:
#                         count += 1
#         return count
# arr = [5,4,3,2,1]
# a = Solution()
# print(a.count_inversions(arr))


'''Brute force'''
# class Solution:
#     def count_inversions(self, arr):
#         n = len(arr)
#         mid = n // 2
#         count = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                     if arr[i] > arr[j]:
#                         count += 1
#         return count
# arr = [5,4,3,2,1]
# a = Solution()
# print(a.count_inversions(arr))



'''My Optimal approach'''
class Solution:
    def merge(self, arr, low, mid, high):
        temp = []
        left, right = low, mid+1
        count = 0
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                count += (mid - left + 1)
                right += 1
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1
        for i in range(low, high+1):
            arr[i] = temp[i - low]
        return count
    

    def merge_sorting(self, arr, low, high):
        count = 0
        if low >= high:
            return count
        mid = (low + high) // 2
        count += self.merge_sorting(arr, low, mid)
        count += self.merge_sorting(arr, mid+1, high)
        count += self.merge(arr, low, mid, high)
        return count
    

    def count_inversions(self, arr):
        return self.merge_sorting(arr, 0, len(arr)-1)
arr = [5,4,3,2,1]
a = Solution()
print(a.count_inversions(arr))
