# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(root):
            elements=[]
            
            if root.left:
                elements+= inorder(root.left)
            
            elements.append(root.val)
            
            if root.right:
                elements+= inorder(root.right)
            
            return elements
        arr=inorder(root)
        minm=max(arr)
        for i in range(1,len(arr)):
            res=arr[i]-arr[i-1]
            minm=min(minm,res)
        return minm