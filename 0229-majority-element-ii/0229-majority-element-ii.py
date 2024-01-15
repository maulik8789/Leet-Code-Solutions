class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d= defaultdict(int)
        for i in nums:
            d[i] += 1
        res = [key for key, value in d.items() if ( value>len(nums)/3)]
        return res