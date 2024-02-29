class Solution:
    def reverseVowels(self, s: str) -> str:
        v='AEIOUaeiou'
        vo=[]
        for l in range(len(s)):
            if s[l] in v:
                vo.append(s[l])
        s=list(s)
        for l in range(len(s)):
            if s[l] in v:
                s[l]=vo.pop(-1)
        return ''.join(s)