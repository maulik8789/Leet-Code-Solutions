class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # this problem is solved using suffix array
        left=[1]*len(nums)
        right=[1]*len(nums)
        
        for i in range(1,len(nums)):
            left[i]=left[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            right[i]=right[i+1]*nums[i+1]
        for i in range(len(nums)):
            nums[i]=left[i]*right[i]
        return nums
        
        
        # Time limit Exceeded
        # ans=1
        # res=[]
        # for i in range(len(nums)):
        #     ans=1
        #     for j in range(len(nums)):
        #         if i==j:
        #             continue
        #         ans=ans*nums[j]
        #     res.append(ans)
        # return res