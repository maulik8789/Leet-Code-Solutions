# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Runtime: 382 ms
        dummy=ListNode(0,head)
        
        # start=dummy
        start,slow, fast=dummy,dummy,dummy
        
        for i in range(k):
            start=start.next
            fast=fast.next
        
        while fast:
            fast=fast.next
            slow=slow.next
            
        start.val, slow.val=slow.val, start.val
        return head
        
        
#       Runtime: 390 ms,
        #         arr=[]
#         if not head or not head.next:
#             return head
        
#         def lstLen(header):
#             curr=header
#             while curr:
#                 arr.append(curr.val)
#                 curr=curr.next
        
#         lstLen(head)
        
#         curr=head
#         itr=0
#         endK=len(arr)-k

#         while curr:
#             if k-1==itr:
#                 curr.val=arr[endK]
#             elif endK==itr:
#                 curr.val=arr[k-1]
#             itr+=1
#             curr=curr.next

#         return head