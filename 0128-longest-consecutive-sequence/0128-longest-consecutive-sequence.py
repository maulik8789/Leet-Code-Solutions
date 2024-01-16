class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return 0

        nums.sort()

        cnt = 1
        maxi = 0

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    cnt += 1
                else:
                    maxi = max(maxi, cnt)
                    cnt = 1

        return max(maxi, cnt)


        # Time Limit Exceeded: 66 / 75 testcases passed
        # o=[]
        # if nums==[]:
        #     return 0
        # def consec(list):
        #     o.append([])
        #     o[-1].append(min(nums))
        #     nums.pop(nums.index(o[-1][0]))
        #     for i in range(len(nums)):
        #         if o[-1][-1]+1 in nums:
        #             o[-1].append(nums[nums.index(o[-1][-1]+1)])
        #             nums.pop(nums.index(o[-1][-1]))
        #     if len(nums)>len(o[-1]):
        #         consec(list)
            
                
        #     # print(o)
        #     # print (nums)
        #     # print(len(max(o,key=len)))
        #     # return len(max(o,key=len))
        # consec(nums)
        # return len(max(o,key=len))