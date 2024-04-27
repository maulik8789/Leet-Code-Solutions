# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr=[]
        if not head or not head.next:
            return head
        def lstLen(header):
            
            curr=header
            l=0
            while curr:
                l+=1
                arr.append(curr.val)
                curr=curr.next
            return l
        
        lenL=lstLen(head)
        
        curr=head
        itr=0
        endK=lenL-k
        

        while curr:
            if k-1==itr:
                curr.val=arr[endK]
                # temp1=curr.val
            elif endK==itr:
                curr.val=arr[k-1]
                # temp2=curr.val
            itr+=1
            
            curr=curr.next

        return head