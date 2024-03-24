class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        counter=0
        reqPos=1
        # startPoint=min(nums)
        print(list(set(nums)))
        nums=list(set(nums))
        nums.sort()
        print(nums)
        i=0
        while i<len(nums):
            if nums[i]!=reqPos and nums[i]>0:
                return reqPos
            elif nums[i]<=0:
                i+=1
            else:
                reqPos+=1
                i+=1
            print(i,reqPos)
        # while i<len(nums):
        #     if reqPos not in nums:
        #         return reqPos
        #     else:
        #         reqPos+=1
        #     i+=1
        return reqPos