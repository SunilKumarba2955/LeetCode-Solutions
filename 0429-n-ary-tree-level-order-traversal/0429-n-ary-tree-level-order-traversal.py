"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            temp = []
            r = []
            for i in queue:
                r.append(i.val)
                for j in i.children:
                    temp.append(j)
            res.append(r)
            queue = temp
        return res