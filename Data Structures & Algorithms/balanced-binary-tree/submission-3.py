# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return [0, True]
            
            left, leftBalanced = dfs(node.left)
            right, rightBalanced = dfs(node.right)

            if not (leftBalanced and rightBalanced):
                return [1 + max(left, right), False]

            if -1 <= left - right <= 1:
                return [1 + max(left, right), True]
            else:
                return [1 + max(left, right), False]

        return dfs(root)[1]

        