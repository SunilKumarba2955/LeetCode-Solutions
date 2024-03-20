# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ptr3 = list2
        while ptr3.next:
            ptr3 = ptr3.next
        ptr1 = list1
        for i in range(a-1):
            ptr1 = ptr1.next
        ptr2 = ptr1
        for i in range(a, b+2):
            ptr2 = ptr2.next
        # ptr2 = ptr2.next
        ptr1.next = list2
        ptr3.next = ptr2
        return list1