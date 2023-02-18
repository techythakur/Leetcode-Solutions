# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap(curr):
            if not curr:
                return
            
            swap(curr.left)
            swap(curr.right)
            
            temp=curr.left
            curr.left=curr.right
            curr.right=temp
        
        swap(root)
        return root