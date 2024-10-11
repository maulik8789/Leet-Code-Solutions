class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m=float('-inf')
        s=0
        for i in nums:
            s+=i
            m=max(m,s)
            if s<0:
                s=0
        return m