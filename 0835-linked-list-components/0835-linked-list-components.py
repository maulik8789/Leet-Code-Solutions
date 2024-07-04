# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        curr=head
        sub_arr=[[]]
        while curr:
            if curr.val in nums:
                sub_arr[-1].append(curr.val)
            elif curr.next is not None and len(sub_arr[-1])>0:
                sub_arr.append([])
            curr=curr.next
        print(sub_arr)
        if sub_arr[-1]==[]:
            sub_arr.pop()
        return len(sub_arr)