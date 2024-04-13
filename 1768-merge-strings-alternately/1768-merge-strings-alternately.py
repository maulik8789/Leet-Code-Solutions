class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        remainWord2=0
        if len(word1)<len(word2):
            l=len(word1)
            remainWord2=1
        else:
            l= len(word2)
        
        ans=''
        for c in range(l):
            ans+=word1[c]+word2[c]
        
        if remainWord2:
            ans+=word2[c+1:]
        else:
            ans+=word1[c+1:]
        return ans