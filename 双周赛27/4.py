from typing import List
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        from functools import lru_cache
        def next(i, j):
            r = []
            if i + 1 < n and j - 1 >= 0:
                r.append((i + 1, j - 1))
            if i + 1 < n:
                r.append((i + 1, j))
            if i + 1 < n and j + 1 < m:
                r.append((i + 1, j + 1))
            return r
        @lru_cache(None)
        def f(i, j, x, y):
            if i == x and j == y:
                r = grid[i][j]
            else:
                r = grid[i][j] + grid[x][y]
            res = []
            for i1, j1 in next(i, j):
                for x1, y1 in next(x, y):
                    res.append(f(i1, j1, x1, y1))
            if res:
                return r + max(res)
            return r

        return f(0, 0, 0, m - 1)

if __name__ == '__main__':
    print(Solution().cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
    ))
