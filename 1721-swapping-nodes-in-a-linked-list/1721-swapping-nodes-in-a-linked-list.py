# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        def lstLen(header):
            curr=header
            l=0
            while curr:
                l+=1
                curr=curr.next
            return l
        
        lenL=lstLen(head)
        # print(lenL)
        
        curr=head
        itr=0
        endK=lenL-k
        
        temp1,temp2=0,0
        
        while curr:
            if k-1==itr:
                temp1=curr.val
                
            if endK==itr:
                temp2=curr.val
            itr+=1
            
            curr=curr.next
        # print(temp1, temp2, head)
        
        curr1=head
        itr=0
        while curr1:
            if k-1==itr:
                curr1.val=temp2
            if endK==itr:
                curr1.val=temp1
            itr+=1
            # print(curr1)
            curr1=curr1.next
            # print(itr)
            # print(curr1)
        # print(head)
        return head