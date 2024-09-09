import math
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #This is an Example of Dynamic Programming
        #start with first element of the array
        curr_min=nums[0]
        curr_max=nums[0]
        
        ans=curr_max
        
        #start comparing with next element
        for num in nums[1:]:
            temp_min=min(num,num*curr_min,num*curr_max)
            curr_max=max(num,num*curr_min,num*curr_max)
            curr_min=temp_min
            
            ans=max(ans,curr_max)
        return ans
    
#         Using Brute Force
#         # Runtime: 260 ms
#         ans=float('-inf')
#         ans=max(ans,math.prod(nums))
#         if ans>0:
#             return ans
#         ans=max(ans,max(nums))
        
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 # print(nums[i:j+1])
#                 ans=max(ans,math.prod(nums[i:j+1]))
        
#         return ans