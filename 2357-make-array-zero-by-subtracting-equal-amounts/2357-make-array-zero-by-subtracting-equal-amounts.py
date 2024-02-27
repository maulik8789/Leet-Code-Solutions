class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        k=0
        if max(nums)==0:
            return 0
        while max(nums)!=0:
            non_zero_val = [x for x in nums if x != 0]
            for i in range(len(nums)):
                if nums[i]==0:
                    continue
                m=min(non_zero_val)
                nums[i]=nums[i]-m
            k+=1
        return k