class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine)<len(ransomNote):
            return False
        dR=defaultdict(int)
        dm=defaultdict(int)
        # for i in ransomNote:
        #     dR[i]+=1
        # for i in magazine:
        #     dm[i]+=1
        l1=len(magazine)
        l2=len(ransomNote)
        l=max(l1,l2)
        for i in range(l):
            if i<l1:
                dm[magazine[i]]+=1
            if i<l2:
                dR[ransomNote[i]]+=1
        for i in dR.keys():
            if dR[i]>dm[i] or i not in magazine:
                return False
        return True
    
        # Runtime: 153ms
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