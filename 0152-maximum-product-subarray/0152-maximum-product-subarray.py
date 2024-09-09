import math
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=float('-inf')
        ans=max(ans,math.prod(nums))
        if ans>0:
            return ans
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                # print(nums[i:j+1])
                ans=max(ans,math.prod(nums[i:j+1]))
        
        return ans