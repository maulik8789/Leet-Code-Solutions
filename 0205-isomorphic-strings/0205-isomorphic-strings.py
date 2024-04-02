class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sd={}
        td={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in sd:
                if sd[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in td:
                    if td[t[i]]!=s[i]:
                        return False
            
            sd[s[i]]=t[i]
            td[t[i]]=s[i]
        return True
                
            