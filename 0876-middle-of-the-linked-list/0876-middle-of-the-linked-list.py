import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow
        
#         def getLen(header):
#             current=header
#             length=0
            
#             while current:
#                 length+=1
#                 current=current.next
#             return length
        
#         lstLen=getLen(head)
#         curr=head
#         point=1
#         print((lstLen//2))
#         while point<=(lstLen//2):
#             point+=1
#             curr=curr.next
#         return curr