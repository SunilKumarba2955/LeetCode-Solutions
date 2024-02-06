"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root:
            queue = [root]
            while queue:
                temp = []
                for i in range(len(queue)-1):
                    queue[i].next = queue[i+1]
                    if queue[i].left:
                        temp.append(queue[i].left)
                    if queue[i].right:
                        temp.append(queue[i].right)
                queue[-1].next = None
                if queue[-1].left:
                    temp.append(queue[-1].left)
                if queue[-1].right:
                    temp.append(queue[-1].right)
                queue = temp
        return root