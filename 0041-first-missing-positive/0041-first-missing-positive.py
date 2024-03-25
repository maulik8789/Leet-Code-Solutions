class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        reqPos=1
        nums=list(set(nums))
        nums.sort()
        i=0
        while i<len(nums):
            if nums[i]!=reqPos and nums[i]>0:
                return reqPos
            elif nums[i]<=0:
                i+=1
            else:
                reqPos+=1
                i+=1

        return reqPos