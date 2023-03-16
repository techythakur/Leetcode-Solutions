# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        ip = len(inorder) - 1
        pp = len(postorder) - 1

        st = []
        prev = None
        root = TreeNode(postorder[pp])
    
        st.append(root)
        pp -= 1

        while pp >= 0:
            
            while st and st[-1].val == inorder[ip]:
                
                prev = st.pop()
                ip -= 1
            new_node = TreeNode(postorder[pp])
            if prev:
                prev.left = new_node
            elif st:
                curr_top = st[-1]
                curr_top.right = new_node
            
            st.append(new_node)
            prev = None
            pp -= 1

        return root
