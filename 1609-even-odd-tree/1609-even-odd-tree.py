# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        level = 0
        while queue:
            temp = []
            prev = None
            for i in queue:
                if level%2==0:
                    if i.val%2==0 or (prev!=None and i.val<=prev):
                        return False
                    else:
                        prev = i.val
                else:
                    if i.val%2!=0 or (prev!=None and i.val>=prev):
                        return False
                    else:
                        prev = i.val
                if i.left: temp.append(i.left)
                if i.right: temp.append(i.right)
            level+=1
            queue = temp
        return True