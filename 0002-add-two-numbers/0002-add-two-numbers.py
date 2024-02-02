# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
                self.head=None
                
            def insert_at_top(self,val):
                node=ListNode(val,self.head)
                self.head=node
            
            def print(self):
                if self.head==None:
                    print(LinkList is empty)
                    return
                
                itr=self.head
                llstr=str(itr.val)
                itr=itr.next
                
                while itr:
                    llstr=llstr+' ---> '+str(itr.val)
                    itr=itr.next
                # print(llstr)
            
            def linklist_to_int(self):
                result=0
                curr=self.head
                while curr is not None:
                    result=result*10+curr.val
                    curr=curr.next
                return result
            def int_to_list(self,num):
                # temp_head=ListNode()
                # curr=temp_head
                s=str(num)
                for i in s:
                    self.insert_at_top(i)
                
        # l=LinkList()
        # l.insert_at_top(4)
        # l.insert_at_top(2)        
        # l.insert_at_top(1)        
        # l.print()
        
        ll1=ListNode()
        curr=l1
        while curr is not None:
            ll1.insert_at_top(curr.val)
            curr=curr.next
        # ll1.print()
        
        ll2=ListNode()
        curr=l2
        while curr is not None:
            ll2.insert_at_top(curr.val)
            curr=curr.next
        # ll2.print()
        # print(ll1.linklist_to_int() + ll2.linklist_to_int())
        ans=ListNode()
        ans.int_to_list(ll1.linklist_to_int() + ll2.linklist_to_int())
        # ans.print()
        return ans.head