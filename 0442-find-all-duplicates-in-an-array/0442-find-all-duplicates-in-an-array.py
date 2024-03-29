class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d=defaultdict(int)
        ans=set()
        for i in nums:
            d[i]+=1
            if d[i]>1:
                  ans.add(i)
        return list(ans)