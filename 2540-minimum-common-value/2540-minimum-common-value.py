class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        d=Counter(nums1)
        # print(d)
        for i in nums2:
            if i in d:
                return i
        return -1
            
        
        # for i in range(len(nums1)):
        #     if nums1[i] < nums2[0]:
        #         continue
        #     if nums1[i] in nums2:
        #         return nums1[i]
        # return -1