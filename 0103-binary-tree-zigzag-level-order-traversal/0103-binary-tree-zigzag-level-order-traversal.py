# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        level = 1
        while queue:
            temp = []
            r = []
            for i in queue:
                r.append(i.val)
                if i.left: temp.append(i.left)
                if i.right: temp.append(i.right)
            if level%2==0:
                res.append(r[::-1])
            else:
                res.append(r)
            level+=1
            queue = temp
        return res