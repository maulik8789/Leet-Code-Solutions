# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None or right==left:
            return head
        if head.next.next is None:
            if right==1 or (left==2 and right ==2):
                return head
            elif (left==1 and right==2):
                n=ListNode(head.val)
                temp=head.next
                temp.next=n
                return temp
        
        i=1
        leftNs=[]
        rightNs=[]
        curr=head
        while i<left:
            leftNs.append(ListNode(curr.val))
            curr=curr.next
            i+=1
        # print('l',leftNs)
        while i<left:
            curr=curr.next
            i+=1
        subL=curr
        ans=ListNode(subL.val)
        temp=ans
        while i!=right:
            # temp=temp.next
            temp.next=ListNode(subL.next.val)
            temp=temp.next
            subL=subL.next
            i+=1
        temp.next=None 
        subL=subL.next
        # print(ans)
        while subL:
            rightNs.append(ListNode(subL.val))
            subL=subL.next
            i+=1
        # print('r', rightNs)
        curr=ans
        prev=None
        
        while curr:
            frw=curr.next
            curr.next=prev
            prev=curr
            curr=frw
        # print(prev)
        l=len(leftNs)-1
        new_node=None
        while l>=0 and len(leftNs)>0:
            new_node=None
            new_node = ListNode(leftNs[l].val)
            # print(new_node)
            new_node.next=prev
            prev=new_node
            l-=1
            # print(prev)
        lastCurr=None
        if new_node:
            lastCurr=new_node
        else:
            lastCurr=prev
        if lastCurr:
            while lastCurr.next:
                lastCurr=lastCurr.next
        # print(lastCurr)
        # if lastCurr:
        l=0
        while l<len(rightNs) and len(rightNs)>0:
            # lastCurr=None
            newN=ListNode(rightNs[l].val)
            lastCurr.next=newN
            # print(lastCurr)
            # print(new_node)
            lastCurr=lastCurr.next
            l+=1
        # print(prev)
        return new_node if new_node else prev
            