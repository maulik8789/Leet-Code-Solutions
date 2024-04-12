class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stck=[]
        for i in range(len(temperatures)):
            while stck and temperatures[i]>temperatures[stck[-1]]:
                ind=stck.pop()
                # print(i, ind)
                ans[ind]=i-ind
                # print('ans ',ans)
            stck.append(i)
            # print(stck)
        return ans
    
    
    
    

#         # Time Limit Exceeded
#         op=[]
        
#         for i in range(len(temperatures)):
#             isWarm=0
#             for j in range(i+1,len(temperatures)):
#                 if temperatures[i]<temperatures[j]:
#                     op.append(j-i)
#                     isWarm=1
#                     break
#             if not isWarm:
#                 op.append(0)
#         return op