class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s)==1:
            return 0 
        d=defaultdict(int)
        for i in range(len(s)):
            d[s[i]]+=1
        
        for i in range(len(s)):
            if d[s[i]]==1:
                return s.index(s[i])
        return -1
                      
        