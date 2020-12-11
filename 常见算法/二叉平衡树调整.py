# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        while abs(self.get_depth(root.left) - self.get_depth(root.right)) > 1:
            
    def get_depth(self, node, dep=0):
        if not node:
            return dep
        dep += 1
        return max(self.get_depth(node.left, dep), self.get_depth(node.right, dep))
