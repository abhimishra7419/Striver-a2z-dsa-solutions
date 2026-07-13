'''Brute force'''
# class Solution:
#     def maximam_profit(self, arr):
#         n = len(arr)
#         profit = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 profit = max(profit, arr[j]-arr[i])
#         return f"profit is {profit}"

# arr = [7,6,4,3,1]
# arr1 = [7,1,5,3,6,4]
# a = Solution()
# print(a.maximam_profit(arr))
# print(a.maximam_profit(arr1))



'''My approach'''
# class Solution:
#     def maximam_profit(self, arr):
#         n = len(arr)
#         lowest = float('inf')
#         largest = 0
#         for i in range(n):
#             if lowest > arr[i]:
#                 lowest = arr[i]
#                 buyday = i+1
#         if buyday >= n:
#             return print("There is no profit")
#         for j in range(buyday, n):
#             if lowest < arr[j]:
#                 largest = max(largest, arr[j])
#                 sellday = j
#         if largest <= lowest:
#             return print("there is no profit")
#         else:
#             print(f"The buy day is {buyday} and price is {lowest}")
#             print(f"The sell day is {sellday} and on price {largest}")
#             print(f"With the profit of {largest - lowest}")

# arr = [7,6,4,3,1]
# a = Solution()
# a.maximam_profit(arr)


'''Optimal approach'''
class Solution:
    def maximam_profit(self, arr):
        lowest = float('inf')
        max_profit = 0
        for prices in arr:
            if prices < lowest:
                lowest = prices
            else:
                max_profit = max(max_profit, prices-lowest)
        return max_profit
arr = [7,6,4,3,1]
arr1 = [7,1,5,3,6,4]
a = Solution()
print(a.maximam_profit(arr))
print(a.maximam_profit(arr1))