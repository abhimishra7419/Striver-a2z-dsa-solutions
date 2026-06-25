# class Solution:
#     def sort(self, arr):
#       n = len(arr)
#       if n == 0 or n == 1:
#         print(-1, -1)
#     arr.sort()
#     return f"Second Smallest element is {arr[1]} \nSecond Largest element is {arr[-2]}"
# arr = [1, 3, 5, 3, 5, 6, 7, 8, 9, 7, 54]
# a = Solution()
# print(a.sort(arr))

class Solution:
    def large_small(self, arr):
        n = len(arr)
        if n == 0 or n == 1:
            print(-1, -1)
            return
        smallest = float("inf")    # initializing infinite
        second_smallest = float("inf")
        largest = float("-inf")    # initializing "-" infinite
        second_largest = float("-inf")

        for i in range(n):
            smallest = min(smallest, arr[i])
            largest = max(largest, arr[i])
        for i in range(n):
            if arr[i] <= second_smallest and smallest != arr[i]:
                second_smallest = arr[i]
            if arr[i] >= second_largest and largest != arr[i]:
                second_largest = arr[i]
        print("The second smallest element is :",second_smallest)
        print("The second largest element is :",second_largest)
a = Solution()
a.large_small([2, 4, 6, 6, 8, 6, 4, 2, 7, 5, 3, 2, 5, 4, 2, 4, 2, 98, 9])