class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        arr=[]
        for i in range(len(l)):
            # print(l[i],r[i])
            arr.append(sorted(nums[l[i]:r[i]+1]))
        print(arr)
        ans=[]
        for i in range(len(arr)):
            # print(arr[i],arr[i])
            diff=arr[i][0]-arr[i][1]
            isFalse=0
            for j in range(1,len(arr[i])):
                if diff==arr[i][j-1]-arr[i][j]:
                    continue
                else:
                    ans.append(False)
                    isFalse=1
                    break
            if not isFalse:
                ans.append(True)
        return ans