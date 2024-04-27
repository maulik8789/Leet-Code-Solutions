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
            # l=0
            while curr:
                # l+=1
                arr.append(curr.val)
                curr=curr.next
            # return l
        
        lstLen(head)
        
        curr=head
        itr=0
        endK=len(arr)-k

        while curr:
            if k-1==itr:
                curr.val=arr[endK]
            elif endK==itr:
                curr.val=arr[k-1]
            itr+=1
            curr=curr.next

        return head