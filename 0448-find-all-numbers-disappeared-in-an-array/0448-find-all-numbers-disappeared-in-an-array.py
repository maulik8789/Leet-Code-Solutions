class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s=set(nums)
        l=len(nums)
        ans=[]
        
        for i in range(l):
            if i+1 not in s:
                ans.append(i+1)
        return ans