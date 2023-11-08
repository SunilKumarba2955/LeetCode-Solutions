# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
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
            heapq.heappush(res, sum)
            if len(res)>k:
                heapq.heappop(res)
            stack = temp
        return res[0] if len(res)>=k else -1