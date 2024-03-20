# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        def getLen(header):
            current=header
            length=0
            
            while current:
                length+=1
                current=current.next
            return length
        
        lstLen=getLen(head)
        # if lstLen<2:
            # return None
        curr=head
        point=1
        # print((lstLen//2))
        # print(head)
        # while point<=(lstLen//2):
        while curr:
            if point==(lstLen//2):
                curr.next=curr.next.next
                break
            else:    
                point+=1
                curr=curr.next
        # print(curr)
        return head