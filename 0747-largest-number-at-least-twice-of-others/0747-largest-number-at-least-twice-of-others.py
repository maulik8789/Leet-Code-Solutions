class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxNInd=nums.index(max(nums))
        maxN=nums.pop(maxNInd)
        return maxNInd if maxN>=max(nums)*2 else -1