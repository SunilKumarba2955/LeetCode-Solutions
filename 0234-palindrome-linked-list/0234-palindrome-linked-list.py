# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self, tempHead: Optional[ListNode]) -> Optional[ListNode]:
        nxt = tempHead.next if tempHead else tempHead
        cur = tempHead
        if cur:
            cur.next = None
        while nxt:
            temp = nxt.next
            nxt.next = cur
            cur = nxt
            nxt = temp

        return cur
            
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow, fast, prev = head, head, None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None
        temp = slow.next if fast else slow
        head1, head2 = head, self.reverse(temp)
        while head1 and head2 and head1.val == head2.val:
            head1 = head1.next
            head2 = head2.next
        return False if head1 and head2 else True