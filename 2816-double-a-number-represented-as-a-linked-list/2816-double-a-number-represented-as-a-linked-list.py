# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st, d = [], 0

        while head:
            st.append(head.val)
            head = head.next
        
        while len(st) > 0:
            num = 2 * st.pop() + d
            d = 1 if num >= 10 else 0
            head = ListNode(num % 10, head)
        
        if d == 1:
            head = ListNode(d, head)
        
        return head
        # Runtime: 569 ms,
#         sys.set_int_max_str_digits(1000000)
#         n=0
#         i=0
#         curr=head
#         while curr:
#             n=(n*(10))+curr.val
#             i+=1
#             curr=curr.next
        
#         n=n*2
#         n=str(n)
#         i=0
#         newNode=ListNode()
#         cur=newNode
#         while len(n):
#             cur.val=n[i]
#             i+=1
#             if i==len(n):
#                 break
#             cur.next=ListNode()
#             cur=cur.next
#         return newNode