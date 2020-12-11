from typing import List
class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        from collections import defaultdict
        from functools import lru_cache
        pre = defaultdict(set)
        for i, j in prerequisites:
            pre[j].add(i)

        res = []
        @lru_cache(None)
        def dfs(i, j):
            if not pre[j]:
                return False

            if i in pre[j]:
                return True
            for k in pre[j]:
                if dfs(i, k):
                    return True
            return False

        for i, j in queries:
            res.append(dfs(i, j))
        return res
