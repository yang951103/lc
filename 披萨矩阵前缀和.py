from typing import List
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        n, m = len(pizza), len(pizza[0])
        g = [[0] * m for _ in range(n)]
        g[0][0] = int(pizza[0][0] == 'A')
        for i in range(1, m):
            g[0][i] += g[0][i-1] + int(pizza[0][i] == 'A')
        for i in range(1, n):
            g[i][0] += g[i-1][0] + int(pizza[i][0] == 'A')
        for i in range(1, n):
            for j in range(1, m):
                g[i][j] += g[i][j-1] + g[i-1][j] - g[i-1][j-1] + int(pizza[i][j] == 'A')
        print(g)

if __name__ == '__main__':
    print(Solution().ways(["A..","AAA","..."], 3))

