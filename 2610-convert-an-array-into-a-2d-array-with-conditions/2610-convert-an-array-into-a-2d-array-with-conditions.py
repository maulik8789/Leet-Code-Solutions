class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        for i in range(len(nums)):
            for j in range(len(ans)):
                if nums[i] not in ans[j]:
                    ans[j].append(nums[i])
                    break
                    # ans.append([nums[i]])
                elif j==len(ans)-1:
                    ans.append([nums[i]])
        return ans