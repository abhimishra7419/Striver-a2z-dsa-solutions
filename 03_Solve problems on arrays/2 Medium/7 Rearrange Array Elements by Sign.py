'''My approach and Brute force'''
# class Solution:
#     def rearranging(self, arr):
#         pos_arr = []
#         neg_arr = []
#         n = len(arr)
#         for i in range(n):
#             if arr[i] >= 0:
#                 pos_arr.append(arr[i])
#             else:
#                 neg_arr.append(arr[i])

#         for i in range(n//2):
#             arr[2*i] = pos_arr[i]
#             arr[2*i+1] = neg_arr[i]
#         return arr
# arr = [1, 2, -3, -1, -2, 3]
# a = Solution()
# print(a.rearranging(arr))

'''Optimal approach'''
class Solution:
    def rearranging(self, arr):
        n = len(arr)
        temp_arr = [0]*n
        pos_index = 0
        neg_index = 1
        for num in arr:
            if num > 0:
                temp_arr[pos_index] = num
                pos_index += 2
            else:
                temp_arr[neg_index] = num
                neg_index += 2
        return temp_arr
arr = [1, 2, -3, -1, -2, 3]
a = Solution()
print(a.rearranging(arr))