from typing import List
from functools import lru_cache


class Solution:
    def getProbability(self, balls: List[int]) -> float:
        n = sum(balls)
        tt = 1
        for i in range(1, n+1):
            tt *= i
        def nt(j):
            res = 1
            for i in range(1, j+1):
                res *= i
            return res
        # for i in balls:
        #     tt //= nt(i)
        res = 1
        while n:
            res *= n * (n-1)
            n -= 2
        return res / tt


if __name__ == '__main__':
    print(Solution().getProbability([3,2,1]))
