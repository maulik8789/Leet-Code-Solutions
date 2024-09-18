class Solution:
    def checkRecord(self, s: str) -> bool:
        d=defaultdict()
        d['A']=0
        for c in s:
            if c=='A':
                d['A']+=1
        
        if len(s)<2:
            return True
        if d['A']>=2 or 'LLL' in s or ('P' not in s and 'L' not in s):
            return False
        return True