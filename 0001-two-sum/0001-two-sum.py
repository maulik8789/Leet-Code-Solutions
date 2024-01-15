class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        l=len(nums)
        while i<l-1:
            j=i+1
            while j<l:
                if nums[i]+nums[j]==target :
                    return [i,j]
                j+=1
            i+=1