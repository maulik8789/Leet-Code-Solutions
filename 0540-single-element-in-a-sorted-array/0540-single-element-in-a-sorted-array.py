class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        isChange=0
        i=0
        while i < (len(nums)):
            if i==len(nums)-1:
                return nums[-1]
            elif nums[i]==nums[i+1]:
                i+=1
            else:
                return nums[i]
            i+=1
        return 0
            
            