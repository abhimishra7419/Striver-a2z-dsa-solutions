class Solution:
    def maximum_subarray(self, arr):
        n = len(arr)
        sum = 0
        max_sum = 0
        start = 0
        anstart = -1
        enstart = -1
        for i in range(n):
            if sum == 0:
                start = i

            sum += arr[i]

            if sum > max_sum:
                max_sum = sum
                anstart = start
                enstart = i
            
            if sum < 0:
                sum = 0
        print("[", end="")
        for i in range(anstart , enstart+1):
            print(f"{arr[i]}", end=", ")
        print("]: ", end="")
        return max_sum
arr = [2, 3, -7, 4, 7, -4]
arr2 = [2, 3, 5, -2, 7, -4]
arr3 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
a = Solution()
print(a.maximum_subarray(arr))
print(a.maximum_subarray(arr2))
print(a.maximum_subarray(arr3))