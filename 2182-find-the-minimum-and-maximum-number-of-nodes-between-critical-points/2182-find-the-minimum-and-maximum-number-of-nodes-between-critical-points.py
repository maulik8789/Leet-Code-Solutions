# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr = head
        minArr=[]
        nodeNum=1
        while curr.next.next:
            if curr.next.val<curr.val and curr.next.val<curr.next.next.val:
                minArr.append(nodeNum+1)
            elif curr.next.val>curr.val and curr.next.val>curr.next.next.val:
                minArr.append(nodeNum+1)
            nodeNum+=1
            curr=curr.next
        print(minArr)
        ans=[10000000,-1]
        minArr=sorted(minArr)
        for i in range(len(minArr)-1):
            # for j in range(i+1,len(minArr)):
            frstEle=abs(minArr[i]-minArr[i+1])
            if ans[0]>frstEle:
                ans[0]=frstEle
            # if ans[1]<frstEle:
            #     ans[1]=frstEle
        if len(minArr)>0:
            ans[1]=minArr[-1]-minArr[0]
        return ans if ans[0]!=10000000 else [-1,-1]