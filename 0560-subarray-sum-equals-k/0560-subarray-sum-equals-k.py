class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum =[0] * (len(nums)+1)
        d=defaultdict(int)
        d[0] = 1
        pSum = 0
        cnt = 0
        for i in range(len(nums)):
            pSum += nums[i]
            rem = pSum - k
            cnt += d[rem]
            d[pSum] += 1
            
        return cnt