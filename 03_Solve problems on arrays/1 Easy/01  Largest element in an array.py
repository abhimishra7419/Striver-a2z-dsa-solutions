# class Solution:
#     def QuickSort(self, arr, low, high):
#         if low < high:
#             partitionindex = self.partition(arr, low, high)
#             self.QuickSort(arr, low, partitionindex-1)
#             self.QuickSort(arr, partitionindex+1, high)
#             return arr[high]

#     def partition(self, arr, low, high):
#         pivot = arr[high]
#         i = low - 1
#         for j in range(low, high):
#             if arr[j] <= pivot:
#                 i += 1
#                 arr[i], arr[j] = arr[j], arr[i]
#         arr[i+1], arr[high] = arr[high], arr[i+1]
#         return i+1

'''These two programe are same'''

class Solution:
    def Larest_element(self, arr):
        arr.sort()
        return arr[-1]
    
arr = [3, 5, 7, 4, 2, 6, 7, 4, 7, 8, 9, 9]
a = Solution()
# print(a.QuickSort(arr, 0, len(arr)-1))
print(a.Larest_element(arr))
# print(arr)
