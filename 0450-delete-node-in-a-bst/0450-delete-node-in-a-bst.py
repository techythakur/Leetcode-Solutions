# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val==key:
            if not root.left and not root.right: return None
            if not root.left and root.right: return root.right
            if not root.right and root.left: return root.left
            
            temp=root.right
            while temp.left is not None: 
                temp=temp.left
            root.val=temp.val
            root.right=self.deleteNode(root.right,root.val)
            
        elif key<root.val:
            if root.left:
                root.left=self.deleteNode(root.left,key)
        else:
            if root.right:
                root.right=self.deleteNode(root.right,key)
        
        return root