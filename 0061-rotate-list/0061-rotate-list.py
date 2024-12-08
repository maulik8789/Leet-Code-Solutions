# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        elif k == 0:
            return head
        def lenList(node):
            l = 0
            while node:
                l+=1
                node = node.next
            return l
        
        k = k % lenList(head)
        # print(lenList(head))
        # print(k)
        # print(1%1)
        if k==0:
            return head
        
        # temp = None
        # curr = head
        while k > 0:
            temp = None
            curr = head
            while curr:

                if curr.next.next is None:
                    temp = curr.next
                    curr.next = None
                    temp.next = head
                    # print(temp)
                    break
                else: 
                    curr = curr.next
            head = temp
            k-=1
        return temp