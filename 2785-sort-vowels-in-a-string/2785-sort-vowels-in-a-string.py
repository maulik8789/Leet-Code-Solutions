class Solution:
    def sortVowels(self, s: str) -> str:
        d=defaultdict(int)
        vo=[]
        ind=[]
        v=['A','E','I','O','U','a','e','i','o','u']
        for l in range(len(s)):
            if s[l] in v:
                vo.append(s[l])
                ind.append(l)
        if len(vo)==0:
            return s
        vo.sort()
        k=0
        s=list(s)
        for l in range(len(s)):
            if k>len(vo)-1:
                break
            if l==ind[k]:
                s[l]=vo[k]
                k+=1
        return ''.join(s)