# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Use two pointers technique to find the middle of the list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        prev = None
        curr = slow.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # Disconnect the first half from the reversed second half
        slow.next = None 
        
        # Merge the first half and the reversed second half
        sHalf = prev
        fHalf = head
        while sHalf:
            # Save the next nodes temporarily
            temp1 = fHalf.next
            temp2 = sHalf.next

            # Reorder the nodes
            fHalf.next = sHalf
            sHalf.next = temp1

            # Move the pointers forward
            fHalf = temp1
            sHalf = temp2
            
        # No return needed, modification is done in-place
        