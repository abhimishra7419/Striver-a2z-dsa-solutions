'''Brute force'''
# class Solution:
#     def minimise_max_Distance(self, arr, k):
#         n = len(arr)
#         how_many = [0] * (n - 1)
#         for _ in range(k):
#             max_section = -1
#             max_index = -1

#             for i in range(n-1):
#                 diff = arr[i+1] - arr[i]
#                 section_lenth = diff/(how_many[i] + 1)
#                 if section_lenth > max_section:
#                     max_section = section_lenth
#                     max_index = i
#             how_many[max_index] += 1
        
#         max_ans = -1
#         for i in range(n-1): 
#             diff = arr[i+1] - arr[i]
#             section_lenth = diff / (how_many[i] + 1)   # we can say Number of section = how_many(new section)+ 1
#             max_ans = max(max_ans, section_lenth)
#         return max_ans, how_many

                
# arr = [1, 2, 3, 4, 5, 9]
# k = 2
# a = Solution()
# print(a.minimise_max_Distance(arr, k))

'''Better Approach'''
# import heapq
# class Solution:
#     def minimise_max_Distance(self, arr, k):
#         n = len(arr)
#         how_many = [0] * (n - 1)
#         pq = []
#         for i in range(n-1):
#             dist = arr[i+1] - arr[i]
#             heapq.heappush(pq, (-dist, i))
        
#         for _ in range(k):
#             newdist , index = heapq.heappop(pq)
#             how_many[index] += 1
#             totaldist = arr[index+1] - arr[index]
#             newdist = totaldist / (how_many[index] + 1)
#             heapq.heappush(pq, (-newdist, index))
#         return -pq[0][0], pq
# arr = [1, 2, 3, 4, 5, 9]
# k = 2
# a = Solution()
# print(a.minimise_max_Distance(arr, k))



'''Optimal Approach'''
class Solution:
    def Number_of_gas_station_requried(self, arr, dist):
        n = len(arr)
        count = 0
        for i in range(1, n):
            Number_in_between = int((arr[i] - arr[i-1]) / dist)
            if (arr[i] - arr[i-1]) == (dist * Number_in_between):
                Number_in_between -= 1
            count += Number_in_between
        return count 
    def minimise_max_Distance(self, arr, k):
        low = 0
        high = max(arr[i+1] - arr[i] for i in range(len(arr)-1))
        diff = 1e-6     # (10**(-6)) = 1e-6
        while high - low > diff:
            mid = (low + high) / 2.0
            count = self.Number_of_gas_station_requried(arr, mid)
            if count > k:
                low = mid
            else:
                high = mid
        return high
arr = [1, 2, 3, 4, 5, 9]
k = 2
a = Solution()
print(a.minimise_max_Distance(arr, k))