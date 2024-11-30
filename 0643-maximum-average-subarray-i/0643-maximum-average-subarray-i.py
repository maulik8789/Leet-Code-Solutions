class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        n=len(nums)

        windowSum=sum(nums[:k])
        maxSum=windowSum

        max_start_ind=0
        
        for i in range(n-k):
            windowSum = windowSum - nums[i] + nums[i+k]
            if windowSum > maxSum:
                maxSum = windowSum
                max_start_ind+=1
        
        # print(maxSum)
        return maxSum/k