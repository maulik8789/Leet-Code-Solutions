class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        num=''
        ans=[]
        for char in range(len(s)):
            if s[char].isdigit():
                num+=s[char]
            if (s[char]==' ' or char==len(s)-1) and len(num)>0:
                if int(num) in ans:
                    return False
                ans.append(int(num))
                if max(ans)!=ans[-1]:
                    return False
                num=''

        return True