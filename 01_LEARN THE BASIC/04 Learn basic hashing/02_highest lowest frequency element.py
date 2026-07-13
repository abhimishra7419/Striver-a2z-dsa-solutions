# class solution():
#     def freq(self, arr):
#         n = len(arr)
#         visited = [False]*n
#         maxfreq = 0
#         minfreq = n
#         maxrepated = 0
#         minrepated = 0
#         for i in range(n):
#             if visited[i]:
#                 continue
#             count = 1
#             for j in range(i+1, n):
#                 if arr[i] == arr[j]:
#                     visited[j] = True
#                     count += 1
#             if count > maxfreq:
#                 maxfreq = count
#                 maxrepated = arr[i]
#             if count < minfreq:
#                 minfreq = count
#                 minrepated = arr[i]
#         print(f"Maximum repating value is {maxrepated}, and it's repated {maxfreq} times")
#         print(f"Minimum reapitng value is {minrepated}, and it's repated {minfreq} times")

# a = solution()
# a.freq([1, 2, 3, 4, 1, 3, 2,])

# ↑ compaxity is o(N*N)


# ↓ optimal code is
class solution:
    def maxmin(self, arr):
        freq_map = {}
        for i in arr:
            freq_map[i] = freq_map.get(i, 0) +1
        maxfreq = 0
        maxrepating = 0
        minfreq = len(arr)
        minrepating = 0
        for element, count in freq_map.items():
            if count > maxfreq:
                maxfreq = count
                maxrepating = element
            if count < minfreq:
                minfreq = count
                minrepating = element
        print(f"Maximum repating value is {maxrepating}, and it's repated {maxfreq} times")
        print(f"Minimum reapitng value is {minrepating}, and it's repated {minfreq} times")

a = solution()
a.maxmin([1, 2, 3, 4, 1, 3, 2])
