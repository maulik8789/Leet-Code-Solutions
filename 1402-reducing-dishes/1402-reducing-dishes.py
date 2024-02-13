class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        time=1
        ans=0
        maxv=-10000

        for i in range(len(satisfaction)):
            ans=0
            time=1
            for j in range(i,len(satisfaction)):
                ans+=(time*satisfaction[j])
                time+=1
            maxv=max(maxv,ans)

        return 0 if maxv<0 else maxv