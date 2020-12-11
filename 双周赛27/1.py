from typing import List
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.n = n
        self.p = parent

    def getKthAncestor(self, node: int, k: int) -> int:
        import math
        p = node // math.pow(2, k)
        if p == 0:
            return -1
        return p

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
