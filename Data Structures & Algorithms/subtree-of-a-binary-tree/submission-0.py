# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            
            if p.val != q.val:
                return False

            return same(p.left, q.left) and same(p.right, q.right)
        
        def dfs(node):
            if node == None:
                return False
            
            result = same(node, subRoot)

            return result or dfs(node.left) or dfs(node.right)
        
        return dfs(root)
        

