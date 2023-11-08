# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, res):
        if root:
            res.append(root.val)
            res = self.helper(root.left, res)
            res = self.helper(root.right, res)
        return res
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.helper(root, [])