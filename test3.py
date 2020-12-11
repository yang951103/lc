from typing import List
from collections import defaultdict
from functools import lru_cache

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [[0]*target for _ in range(10)]
        for i in range(1, 10):
            for j in range(cost[i], target+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-cost[i]] + cost[i])



if __name__ == '__main__':
    print(Solution().simplifiedFractions(4))
