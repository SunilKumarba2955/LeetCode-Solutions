# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        slow.next = None
        mx = 0
        fhalf = head
        shalf = prev
        while shalf!=None:
            mx = max(mx, fhalf.val+shalf.val)
            shalf = shalf.next
            fhalf = fhalf.next
        return mx
