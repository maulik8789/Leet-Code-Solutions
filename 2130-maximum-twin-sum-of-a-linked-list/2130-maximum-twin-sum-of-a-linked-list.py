# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head or head.next is None:
            return head
        ans=0
        def middleNode(header):
            fast=head
            slow=head
            while fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next
            return slow
        
        def rev(header):
            prev=None
            curr=header
            
            while curr:
                frw=curr.next
                curr.next=prev
                prev=curr
                curr=frw
            return prev
        
        
        midNode=middleNode(head)
        newHead=midNode.next
        midNode.next=None
        
        newHead=rev(newHead)
        
        
        c1 = head
        c2 = newHead
        f1 = None
        f2 = None

        while c1 and c2:
            # Backup
            f1 = c1.next
            f2 = c2.next

            # Linking
            c1.next = c2
            c2.next = f1
            ans=max(ans,c1.val+c2.val)
            # Move
            c1 = f1
            c2 = f2
        return ans