class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ind = 0
        ans = []
        sameParity = [0]
        for a,b in itertools.pairwise(nums):
            # print(a,b)
            
            if a % 2 == b % 2:
                ind += 1
            sameParity.append(ind)
        # print(sameParity)
        for frm, to in queries:
            # print(frm, to)
            ans.append(sameParity[frm] == sameParity[to])
        return ans
#         Time Limit Exceeds
#         ans = [True] * len(queries)
#         badPair = []
#         stack = -1
#         for q in range(len(queries)):
#             isEven = 0
#             stack = -1
#             for i in range(queries[q][0], queries[q][1]+1):
                
#                 isEven = 1 if nums[i] % 2 else 0 

#                 if stack == isEven:
#                     ans[q]=False
#                     break
#                 else:
#                     stack = isEven
                
#         return ans