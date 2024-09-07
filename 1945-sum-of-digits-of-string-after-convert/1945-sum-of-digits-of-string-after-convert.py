class Solution:
    def getLucky(self, s: str, k: int) -> int:
        print(ord('d') -ord('a')+1)        
        sNum=''
        
        for c in s:
            sNum+=str(ord(c)-ord('a')+1)
        # print(sNum)
        
        for i in range(k):
            ans=0
            for c in sNum:
                ans+=int(c)
            sNum=str(ans)
        return ans