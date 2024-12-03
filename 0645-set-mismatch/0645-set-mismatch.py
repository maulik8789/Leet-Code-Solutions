class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = [0] * (len(nums))
        pointer = defaultdict(int)

        for i in range(len(nums)):
            pointer[nums[i]] += 1 
            arr[nums[i]-1] = nums[i]
        ans1 = 0
        
        for key, val in pointer.items():
            if val == 2:
                ans1 = key 
        
        return [ans1, arr.index(0)+1]