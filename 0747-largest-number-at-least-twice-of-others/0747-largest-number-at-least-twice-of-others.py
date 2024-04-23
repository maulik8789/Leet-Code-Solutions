class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxNInd=nums.index(max(nums))
        # maxN=nums.pop(maxNInd) 
        nums.sort()
        return maxNInd if nums[-1]>=nums[-2]*2 else -1