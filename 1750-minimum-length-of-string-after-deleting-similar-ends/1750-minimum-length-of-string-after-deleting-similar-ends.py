class Solution:
    def minimumLength(self, s: str) -> int:
        r=0
        l=len(s)
        while l-r>1 and s[r]==s[l-1]:
            while s[l-1]==s[l-1-1] and l>0:
                l-=1
            while s[r+1]==s[r] and r<l:
                r+=1
            r+=1
            l-=1
        if r==l-1:
            return 1
        return 0 if (l-r<0) else l-r
                