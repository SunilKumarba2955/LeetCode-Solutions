# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tot = 0
    
    def helper(self, root):
        res = [root.val, 1]
        if root.left:
            left = self.helper(root.left)
            res[0]+=left[0]
            res[1]+=left[1]
        if root.right:
            right = self.helper(root.right)
            res[0]+=right[0]
            res[1]+=right[1]
        if res[0]//res[1] == root.val:
            self.tot+=1
        return res

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.tot