class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(k):
        #     nums.insert(0, nums.pop(-1))
        # print(k%len(nums))
        n = len(nums)
        k = k % n
        nums.reverse()
        nums[:k]=nums[:k][::-1]        
        # print(nums)
        nums[k-n:]=nums[k-n:][::-1]

        