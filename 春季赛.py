from typing import List
from collections import defaultdict
class Solution:
    def minJump(self, jump: List[int]) -> int:
        out = []
        d = defaultdict(set)
        ex = defaultdict(set)
        n = len(jump)
        for i in range(n):
            des = i + jump[i]
            if des > n:
                des = n
            d[des].add(i)
            for j in range(i+1, des):
                ex[j].add(i)
            if des >= n:
                out.append(i)
        dp = [0] + [10000] * (n-1)
        for i in range(n):
            if jump[i] + i >= n:
                return dp[i] + 1
            for j in d[i]:
                if dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1

            for j in ex[i]:
                if dp[j] + 2 < dp[i]:
                    dp[i] = dp[j] + 2


if __name__ == '__main__':
    print(Solution().minJump([10000]*10000))
