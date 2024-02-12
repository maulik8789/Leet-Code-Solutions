class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr=[-1]*(len(nums)+1)
        print(arr)
        for i in range(len(nums)):
            arr[nums[i]]=nums[i]
        return arr.index(-1)