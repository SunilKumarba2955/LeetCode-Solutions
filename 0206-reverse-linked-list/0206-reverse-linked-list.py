# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            cur = head
            Next = head.next
            cur.next = None

            while Next:
                temp = Next
                Next = Next.next
                temp.next = cur
                cur = temp
            return cur
        return head