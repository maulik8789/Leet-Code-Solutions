# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fstN=head
        
        while fstN and fstN.next:
            head=head.next
            fstN=fstN.next.next
            # print(head.val, fstN.val)
            
            if head is fstN:
                return True
        return False