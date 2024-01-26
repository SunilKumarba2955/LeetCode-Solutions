# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        res = []
        while queue:
            if queue[-1] is not None:
                res.append(queue[-1].val)
            queue = [j for i in queue if i is not None for j in (i.left, i.right) if j is not None]
        return res
