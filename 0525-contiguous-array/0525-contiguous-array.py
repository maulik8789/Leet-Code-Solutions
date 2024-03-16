class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        one=0
        zero=0
        maxLen=0
        
        d={0:-1}
        
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            else:
                one+=1
            
            dif=zero-one
            
            if dif in d:
                maxLen=max(maxLen,i-d[dif])
            else:
                d[dif]=i
        
        return maxLen
                