'''My approach and also optimal approach'''
class Solution:
    def leader(self, arr):
        n = len(arr)
        lastbigvalue = arr[n-1]
        Leader_arr = [arr[n-1]]
        for i in range(n-2, -1, -1):
                if arr[i] > lastbigvalue:
                    lastbigvalue = arr[i]
                    Leader_arr.append(arr[i])
                else:
                    continue
        for i in range(len(Leader_arr)-1, -1, -1):
            print(Leader_arr[i], end=" ")


arr = [10, 22, 12, 3, 0, 6]
a = Solution()
a.leader(arr)