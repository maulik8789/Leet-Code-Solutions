# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        ans=ListNode()
        ans_head=ans
        tot=0
        while curr:
            if curr.val==0 and tot!=0:
                ans_head.val=tot
                if curr.next:
                    ans_head.next=ListNode()
                    ans_head=ans_head.next
                tot=0
            else:
                tot+=curr.val
            curr=curr.next
        return ans
            