
class Solution:
    def minPartitions(self, n: str) -> int:
        # Shortened version of mathematical solution
        return int(max(n))
        
        # mathematical solution Runtime: 8406 ms

        # ans=-1
        # for i in n:
        #     if int(i)>ans:
        #         ans=int(i)
        # return ans
        
        
        # With actual logic: Runtime: 8406 ms
#         # Increase the limit for integer string conversion
#         sys.set_int_max_str_digits(100000)
#         tot=0
#         tmp=''
#         rep=0
        
#         while n!='0':
#             for i in range(len(n)):
#                 if n[i]!='0':
#                     tmp+='1'
#                 else:
#                     tmp=tmp+'0'
#             tot=int(n)-int(tmp)
#             rep+=1
#             if tot==0:
#                 return rep
#             tmp=''
#             n=str(tot)