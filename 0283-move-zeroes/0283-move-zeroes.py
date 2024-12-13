class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
            right += 1
            # print(nums)
        
        # Runtime: 17ms
#         i, k = 0, 0
        
#         for k in range(len(nums)):
#             if nums[i] == 0:
#                 nums.append(nums.pop(i))
#             else:
#                 i+=1 
        