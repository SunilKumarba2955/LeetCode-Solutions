# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def merge(self, res1, res2):
        res = []
        i,j = 0,0
        while i<len(res1) and j<len(res2):
            if res1[i] == res2[j]:
                res.extend([res1[i]]*2)
                i+=1
                j+=1
            elif res1[i]<res2[j]:
                res.append(res1[i])
                i+=1
            else:
                res.append(res2[j])
                j+=1
        if i<len(res1):
            res.extend(res1[i:])
        if j<len(res2):
            res.extend(res2[j:])
        return res

    def inorder(self, root, res):
        if root:
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res1 = []
        res2 = []
        self.inorder(root1, res1)
        self.inorder(root2, res2)
        return self.merge(res1, res2)