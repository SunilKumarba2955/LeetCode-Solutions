# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, head, l):
        MOD=10**9+7
        if head and head.next:
            l[0] = self.solve(head.next,l)
            l[1] += 1
        return (head.val*(2**(l[1]))+l[0])%MOD
    def getDecimalValue(self, head: ListNode) -> int:
        return self.solve(head, [0,0])