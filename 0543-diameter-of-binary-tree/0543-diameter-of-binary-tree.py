# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def calHeight(root):
            nonlocal maxDiameter
            if not root:
                return 0
            left = calHeight(root.left)
            right = calHeight(root.right)

            maxDiameter = max(maxDiameter, left+right)
            return 1+max(left, right)
        calHeight(root)
        return maxDiameter