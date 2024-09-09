import math
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=float('-inf')
        ans=max(ans,math.prod(nums))
        if ans>0:
            return ans
        ans=max(ans,max(nums))
        
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                # print(nums[i:j+1])
                ans=max(ans,math.prod(nums[i:j+1]))
        
        return ans