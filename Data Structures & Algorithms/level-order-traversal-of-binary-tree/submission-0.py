# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        
        def dfs(node, index):
            if not node:
                return 0
            
            d[index].append(node.val)
            
            dfs(node.left, index + 1)
            dfs(node.right, index + 1)
        
        dfs(root, 0)

        final = []
        for value in d.values():
            final.append(value)
        
        return final

