class Solution:
    def spiral_Traversal(self, matrix):
        result = []
        left = 0
        right = len(matrix[0])-1
        top = 0
        down = len(matrix)-1
        
        while left <= right and top <= down:
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1
            for i in range(top, down+1):
                result.append(matrix[i][right])
            right -= 1
            if left <= right:
                for i in range(right, left-1, -1):
                    result.append(matrix[down][i])
                down -= 1
            if top <= down:
                for i in range(down, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result
arr = [
    [ 1, 2, 3, 4 ],
    [ 5, 6, 7, 8 ],
    [ 9, 10, 11, 12 ],
    [ 13, 14, 15, 16 ]
]
a = Solution()
print(a.spiral_Traversal(arr))