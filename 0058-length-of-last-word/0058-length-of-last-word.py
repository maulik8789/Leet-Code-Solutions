class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans=''
        for c in range(len(s)-1,-1,-1):
            if s[c]!=' ':
                ans=s[c]+ans
            elif s[c]==' ' and ans=='':
                continue
            else:
                return len(ans)
        return len(ans)