class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        a=Counter(nums)
        print(a)

        nums.sort(key=lambda x: (a[x], -x))
        return nums