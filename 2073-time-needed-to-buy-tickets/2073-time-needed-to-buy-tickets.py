class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans=0
        while tickets[k]!=0:
            for i in range(len(tickets)):
                if tickets[i]==0:
                    continue
                if tickets[k]==0:
                    break
                tickets[i]-=1
                # print(tickets)
                ans+=1
        return ans