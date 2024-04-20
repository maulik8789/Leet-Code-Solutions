class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans=0
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        for key, val in d.items():
            if val>1:
                continue
            ans+=key
        return ans