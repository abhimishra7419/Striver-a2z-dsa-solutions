# class solution:
#     def countFreq(self, arr, n):
#         visited = [False] * n
#         for i in range(n):
#             if visited[i]:
#                 continue
#             count = 1
#             for j in range(i + 1, n):
#                 if arr[i] == arr[j]:
#                     visited[j] = True
#                     count += 1
#             print(arr[i], count)
# a = solution()
# a.countFreq([1, 2, 1, 2, 1, 3, 5, 6], 8)

# ↑ it's brute force code with time compexity o(N*N)


''' optimal approach '''
from collections import defaultdict 
class solution():
    def freq(self, arr):
        n = len(arr)
        freqdict = defaultdict(int)
        for i in range(n):              # more optimal is:- # for i in arr:
            freqdict[arr[i]] += 1                                 #freqdict[num] += 1
        for key, value in freqdict.items():
            print(f"{key} -> {value}")
a = solution()
a.freq([1, 2, 3, 4, 1, 3, 2,])