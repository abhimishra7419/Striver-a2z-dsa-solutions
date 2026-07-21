# '''My brute force'''
# class Solution:
#     def finding_median(self, arr1, arr2):
#         for i in range(len(arr2)):
#             arr1.append(arr2[i])
#         arr1.sort()
#         n = len(arr1)
#         if n%2 == 1:
#             return arr1[(n-1)//2]
#         else:
#             mid = (n-1)//2                         # if mid = n//2 then return arr1[mid-1] + arr1[mid]
#             return (arr1[mid] + arr1[mid+1])/2 
# arr1 = [2, 4]
# arr2 = [1, 6]
# a = Solution()
# print(a.finding_median(arr1, arr2))


'''Optimal approach'''
class Solution:
    def finding_median(self, arr1, arr2):
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1
        n1, n2 = len(arr1), len(arr2)
        total = n1+n2
        left = (total+1)//2
        low, high = 0, n1
        while low <= high:
            cut1 = (low+high)//2
            cut2 = left-cut1
            l1 = float('-inf') if cut1 == 0 else arr1[cut1 - 1]
            l2 = float('-inf') if cut2 == 0 else arr2[cut2 - 1]
            r1 = float('inf') if cut1 == n1 else arr1[cut1]
            r2 = float('inf') if cut2 == n2 else arr2[cut2]
            if l1 <= r2 and l2 <= r1:
                if total % 2 == 0:
                    return (max(l1, l2) + min(r1, r2))/2
                else:
                    return max(l1, l2)
            elif l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1
arr1 = [1, 2]
arr2 = [3, 4]
a = Solution()
print(a.finding_median(arr1, arr2))