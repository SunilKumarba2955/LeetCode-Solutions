# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        res = []
        stack = [root]
        while stack:
            sum = 0
            temp = []
            for i in stack:
                sum+=i.val
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            res.append(sum)
            stack = temp
        return res

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res = sorted(self.helper(root))
        print(res)
        return res[-k] if len(res)>=k else -1