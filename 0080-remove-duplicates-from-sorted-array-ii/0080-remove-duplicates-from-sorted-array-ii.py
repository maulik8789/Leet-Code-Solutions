class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        dup=0
        while i<len(nums):
            if nums[i-1]==nums[i]:
                dup+=1
                if dup>=2:
                    nums.pop(i)
                    dup-=1
                    i-=1
            else:
                dup=0
            i+=1
        return len(nums) 
                