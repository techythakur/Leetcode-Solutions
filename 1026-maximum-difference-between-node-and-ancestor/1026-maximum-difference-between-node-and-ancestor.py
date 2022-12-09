# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diff = 0
        
    def maxAncestorDiff(self, root: Optional[TreeNode],mx = -inf, mn = inf) -> int:
        if not root:
            self.diff = max(self.diff, mx - mn)
            return
        mx, mn = max(root.val, mx), min(root.val, mn)
        self.maxAncestorDiff(root.left , mx, mn)
        self.maxAncestorDiff(root.right, mx, mn)
        return self.diff