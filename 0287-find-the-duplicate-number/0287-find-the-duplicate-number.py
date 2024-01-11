class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Runtime: 494ms
        d= defaultdict(int)
        for i in nums:
            d[i] += 1
            if d[i]==2:
                return i

        # Runtime: 512ms
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         return nums[i]