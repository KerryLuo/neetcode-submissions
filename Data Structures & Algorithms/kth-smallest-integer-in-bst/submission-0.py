# recursive dfs probably
# for each node have it also store/return a count of how many nodes it has below it + 1 (total nodes)
# none node returns 0
# bunch of if statements checking:
# k = leftCount + 1, you have your answer
# k <=, search left
# total greater than k, if left less than k, its in the right. Call dfs with target k-leftCount - 1



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def count(node):
            if not node:
                return 0

            return count(node.left) + count(node.right) + 1
        
        def dfs(node, k):
            if not node:
                return 0
            
            left = count(node.left)

            if left + 1 == k:
                return node.val
            elif left >= k:
                return dfs(node.left, k)
            else:
                return dfs(node.right, k - left - 1)
        
        return dfs(root, k)