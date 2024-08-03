class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans=0
        for i in range(len(details)):
            if (details[i][11]+details[i][12]) > '60':
                ans+=1
        return ans