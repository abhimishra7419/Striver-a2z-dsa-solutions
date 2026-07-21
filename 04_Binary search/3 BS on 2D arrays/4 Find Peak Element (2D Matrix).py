'''Opimal approach'''
class Solution:
    def findingRow(self, mat, col, n):
        max_value = float('-inf')
        for i in range(n):
            if max_value < mat[i][col]:
                index = i
                max_value = mat[i][col]
        return index
    def PeakElement(self, mat):
        n = len(mat)
        m = len(mat[0])
        low, high = 0, m-1
        while low <= high:
            mid = (low+high)//2
            row = self.findingRow(mat, mid, n)
            left = mat[row][mid-1] if mid-1 >= 0 else float('-inf')
            right = mat[row][mid+1] if mid+1 < m else float('-inf')

            if left < mat[row][mid] > right:
                return [row, mid]
            elif left > mat[row][mid]:
                high = mid - 1
            else:
                low = mid + 1
        return [-1, -1]
matrix =  [[0,1,2],[7,4,3],[8,5,6]]
a = Solution()
print(a.PeakElement(matrix))