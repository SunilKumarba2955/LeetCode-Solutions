# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
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
        f = head
        s = prev
        while s!=None:
            if s.val!=f.val:
                return False
            s = s.next
            f = f.next
        return True