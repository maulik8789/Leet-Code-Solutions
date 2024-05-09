class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        l=len(score)
        d=defaultdict(int)
        for i in range(l):
            d[score[i]]=i
        
        score=sorted(score)
        ans=['']*(l)
        # print(score,l)
        for i in range(l-1,-1,-1):
            # print(i, d[score[i]],ans)
            if i ==l-1:
                ans[d[score[i]]]='Gold Medal'
            elif i== l-2:
                ans[d[score[i]]]='Silver Medal'
            elif i == l-3:
                ans[d[score[i]]]='Bronze Medal'
            else:
                ans[d[score[i]]]=str(l-i)
        return ans 
            