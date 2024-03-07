# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, temp = None, head
        while temp!=None:
            if temp.val==val:
                if prev!=None:
                    prev.next = temp.next
                else:
                    head = temp.next
                temp = temp.next
            else:
                prev = temp
                temp = temp.next
        return head