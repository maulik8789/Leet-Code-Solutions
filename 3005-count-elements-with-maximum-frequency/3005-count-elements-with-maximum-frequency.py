class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d= defaultdict(int)
        
        for i in nums:
            d[i]+=1
        
        return list(d.values()).count(max(d.values()))*max(d.values())