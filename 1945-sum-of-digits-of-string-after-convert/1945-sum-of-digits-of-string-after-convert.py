class Solution:
    def getLucky(self, s: str, k: int) -> int:
        sNum=''
    
        for c in s:
            sNum+=str(ord(c)-ord('a')+1)
        
        for _ in range(k):
            ans=0
            for c in sNum:
                ans+=int(c)
            sNum=str(ans)
        return ans