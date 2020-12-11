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

        dp = [[[0]*10 for _ in range(m)] for _ in range(n)]
        dp[0][0][1] = 1
        for x in range(2, k+1):
            for i in range(n):
                for j in range(m):
                    if dp[i][j][x] == 0:
                        continue



if __name__ == '__main__':
    print(Solution().ways(["A..","AAA","..."], 3))

