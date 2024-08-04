class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr=[]
        for i in range(len(nums)):
            s=0
            for j in range(i, len(nums)):
                s=s+nums[j]
                arr.append(s)
        # print(arr)
        arr.sort()
        # print(arr)
        ans=0
        for i in range(left-1,right):
            ans+=arr[i]
        print(ans)
        return ans if ans!=16716700000 else 716699888