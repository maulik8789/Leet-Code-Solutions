class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dR=defaultdict(int)
        dm=defaultdict(int)
        for i in ransomNote:
            dR[i]+=1
        for i in magazine:
            dm[i]+=1
            
        for i in dR.keys():
            if dR[i]>dm[i] or i not in magazine:
                return False
        return True
            
        # if len(magazine)<len(ransomNote):
        #     return False
        # d=defaultdict(int)
        # for i in magazine:
        #     d[i] +=1
        # p=0    
        # for key, val in d.items():
        #     if key in ransomNote:
        #         p+=1
        #         if val<ransomNote.count(key):
        #             return False
        # if p==0:
        #     return False
        # return True