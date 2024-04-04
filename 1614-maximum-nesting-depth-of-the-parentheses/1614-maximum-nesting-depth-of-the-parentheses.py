class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        maxD=0
        for i in range(len(s)):
            if s[i]=='(':
                depth+=1
            elif s[i]==')':
                depth-=1
            maxD=max(maxD,depth)

        return (maxD)