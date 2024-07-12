# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_linked_list(head):
            prev = None
            current = head

            while current:
                next_node = current.next  # Store the next node
                current.next = prev       # Reverse the link
                prev = current            # Move prev to current
                current = next_node       # Move current to next node

            return prev
        curr=reverse_linked_list(head)
        ans=ListNode(curr.val)
        temp=ans
        curr=curr.next
        while curr:
            if curr.val<temp.val:
                curr=curr.next
            else:
                temp.next=ListNode(curr.val)
                temp=temp.next
                curr=curr.next
        # print(ans)
        return reverse_linked_list(ans)