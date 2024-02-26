class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        hi=len(nums)-1
        ans=0
        i=0
        while l<hi:
            print(l,hi)
            sm=nums[l]+nums[hi]
            if sm==k:
                ans+=1
                l+=1
                hi-=1
                continue
            if sm>k:
                hi-=1
            else:
                l+=1
            i+=1
        return ans