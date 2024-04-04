class Solution:
    def maxDepth(self, s: str) -> int:
        if s=='()':
            return 1
        countStart=0
        d=defaultdict(str)
        depth=0
        strAns=''
        maxD=0
        for i in range(len(s)):
            if s[i]=='(':
                depth+=1
            elif s[i]==')':
                depth-=1
            maxD=max(maxD,depth)

        return (maxD)