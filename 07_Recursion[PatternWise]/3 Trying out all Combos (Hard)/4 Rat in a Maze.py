''' My appoach '''
class Solution:
    def mazepath(self, curr, i, j, n, m, maze, res):
        if i < 0 or j < 0 or j >= m or i >= n:
            return
        if maze[i][j] == 0:
            return
        if i == (n-1) and j == (m-1):
            res.append("".join(curr))
            return
        maze[i][j] = 0
        curr.append('D')
        self.mazepath(curr, i+1, j, n, m, maze, res)
        curr.pop()
        curr.append('R')
        self.mazepath(curr, i, j+1, n, m, maze, res)
        curr.pop()
        curr.append('U')
        self.mazepath(curr, i-1, j, n, m, maze, res)
        curr.pop()
        curr.append('L')
        self.mazepath(curr, i, j-1, n, m, maze, res)
        curr.pop()
        maze[i][j] = 1
        
    def main(self, maze):
        res = []
        curr = []
        n = len(maze)
        m = len(maze[0])
        self.mazepath(curr, 0, 0, n, m, maze, res)
        if not res:
            return -1
        return res
if __name__ == "__main__":
    grid = [ [1, 0] , [1, 0] ]
    print(Solution().main(grid))