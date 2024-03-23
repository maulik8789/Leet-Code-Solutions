# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr=head
        ans=[]
        
        while curr:
            ans.append(curr.val)
            curr=curr.next
        cur=head
        i=len(ans)-1
        while i>=0:
            if ans[i]!=cur.val:
                return False
            i-=1
            cur=cur.next
        return True