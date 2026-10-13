'''Solution'''
class Solution:
    def graphColoring(self, edges, m, n):
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        color = [-1] * n

        def isSafe(vertex, c):
            for neighbor in adj[vertex]:
                if color[neighbor] == c:
                    return False
            return True

        def solve(vertex):
            if vertex == n:
                return True

            for c in range(m):
                if isSafe(vertex, c):
                    color[vertex] = c
                    if solve(vertex + 1):
                        return True
                    color[vertex] = -1

            return False

        return solve(0)
if __name__ == "__main__":
    N = 4
    M = 3
    Edges = [ (0, 1) , (1, 2) , (2, 3) , (3, 0) , (0, 2) ]
    print(Solution().graphColoring(Edges, M, N))