class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # if len(nums1)<=len(nums2):
        #     d=Counter(nums2)
        #     nums=nums1
        # else:
        d=Counter(nums1)
        nums=nums2
        ans=[]
        for i in nums:
            if i in d:
                if d[i]>0:
                    ans.append(i)
                d[i]-=1
        return (ans)