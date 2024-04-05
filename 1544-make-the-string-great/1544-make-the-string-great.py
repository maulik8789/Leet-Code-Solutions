class Solution:
    def makeGood(self, s: str) -> str:
        i=0
        if len(s)==1:
            return s
        while i<(len(s)-1):
            
            if (s[i]==s[i+1].upper() and not s[i+1].isupper()) or (s[i+1]==s[i].upper() and not s[i].isupper()):
                if i==len(s)-2:
                    s=s[:i]
                else:
                    s=s[:i]+s[i+2:] 
                i-=1
            else:
                i+=1
            if i<0:
                i=0
        return s