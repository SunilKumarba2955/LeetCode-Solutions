# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        res = 0
        while queue:
            temp = []
            for i in queue:
                if i.left:
                    if not i.left.left and not i.left.right:
                        res+=i.left.val
                    else:
                        temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            queue = temp
        return res