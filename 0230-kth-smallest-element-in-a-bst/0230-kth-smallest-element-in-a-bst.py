# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [0]  # Using a list to pass by reference
        def solve(root, k, res):
            if not root:
                return None
            
            left_result = solve(root.left, k, res)
            if left_result is not None:
                return left_result
            
            res[0] += 1
            if res[0] == k:
                return root.val
            
            return solve(root.right, k, res)
        
        return solve(root, k, res)
