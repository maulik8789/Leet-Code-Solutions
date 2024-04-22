class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,k=0,0
        l=len(nums)
        while k <(l)-1:
            if nums[i]==0:
                num=nums.pop(i)
                nums.append(num)
            else:
                i+=1
            k+=1