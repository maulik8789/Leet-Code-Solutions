class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d= defaultdict(int)
        for i in nums:
            d[i] += 1
        res = [key for key, value in d.items() if value == max(d.values())]
        return res[0]