# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            temp = []
            r = []
            for i in queue:
                r.append(i.val)
                if i.left: temp.append(i.left)
                if i.right: temp.append(i.right)
            res.append(r)
            queue = temp
        return res[::-1]