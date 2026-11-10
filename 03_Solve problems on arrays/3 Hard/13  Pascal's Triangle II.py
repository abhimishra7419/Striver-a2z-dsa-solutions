'''Optimal Solution I''' # Using math
# class Solution:
#     def getRow(self, rowIndex: int) -> list[int]:
#         row = [1]
#         for k in range(1, rowIndex + 1):
#             next_val = row[-1] * (rowIndex - k + 1) // k
#             row.append(next_val)
#         return row
# a = Solution()
# r = 4
# print(a.getRow(r))


'''Optimal Solution II'''
# class Solution:
#     def getRow(self, rowIndex: int) -> list[int]:
#         row = [1] * (rowIndex + 1)
        
#         for i in range(2, rowIndex + 1):
#             # Update from right to left to avoid overwriting values needed for the next calculation
#             for j in range(i - 1, 0, -1):
#                 row[j] = row[j] + row[j - 1]
                
#         return row
# a = Solution()
# r = 4
# print(a.getRow(r))
