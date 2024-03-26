# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        if head.val==head.next.val and head.next.next is None:
            return
        dupVal=-sys.maxsize - 1
        current=head
        ans=None
        res=None
        while current:
            if current.next:
                if current.val==current.next.val:
                    dupVal=current.next.val
                    current=current.next
                elif ans is None and current.val!=dupVal:
                    newNode=ListNode(current.val)
                    ans=newNode
                    current=current.next
                    print(ans)
                else:
                    if res is None:
                        res=ans
                    if current.val!=dupVal:
                        res.next=ListNode(current.val)
                        res=res.next
                    current=current.next
                    print(ans)
            elif current.next is None and dupVal!=current.val:
                if res is None:
                    res=ans
                if res is None:
                    ans=ListNode(current.val)
                    res=ans
                    print(res, ans)
                else:
                    res.next=ListNode(current.val)
                res=res.next
                current=current.next
            else:
                current=current.next
        return ans