class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d= defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in d.keys():
                if nums[i] == d[nums[i]][1] and abs(i - d[nums[i]][0]) <= k:
                    return True
            d[nums[i]]=[i,nums[i]]
        return False
        # Time Limit Exceeded
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True
        # return False