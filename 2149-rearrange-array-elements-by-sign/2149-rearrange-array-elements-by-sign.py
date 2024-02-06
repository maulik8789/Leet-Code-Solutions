class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        pos,neg=0,1
        
        for i in range(len(nums)):
            if nums[i]>0:
                ans[pos]=nums[i]
                pos+=2
            else:
                ans[neg]=nums[i]
                neg+=2
        return ans
        
#         # Time Limit Exceeded
        
#         count =1
#         temp=0
#         for i in range(len(nums)):
#             # print(nums[i])
#             # print(nums)
#             if count==1 and nums[i]>0:
#                 # print('1',nums[i])
#                 count =-1
#                 continue
#             elif count==-1 and nums[i]<0:
#                 # print('2',nums[i])
#                 count =1
#                 continue
#             elif count==-1:
                
#                 for j in range(i,len(nums)):
#                     if nums[j]<0:
#                         temp=nums[i]
#                         nums[i]=nums[j]
#                         nums.insert(i+1,temp)
#                         nums.pop(j+1)
#                         count=1
#                         # print('3',nums[i])
#                         break
#             elif count==1:
#                 for j in range(i,len(nums)):
#                     if nums[j]>0:
#                         temp=nums[i]
#                         nums[i]=nums[j]
#                         nums.insert(i+1,temp)
#                         nums.pop(j+1)
#                         count=-1
#                         # print('4',nums[i])
#                         break
#         print(nums)
#         return nums
                
                        