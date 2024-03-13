class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d=Counter(nums1)
        ans=set()
        for i in nums2:
            if i in d:
                ans.add(i)
        return list(ans)