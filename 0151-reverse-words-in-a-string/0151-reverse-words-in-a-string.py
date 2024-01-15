class Solution:
    def reverseWords(self, s: str) -> str:
        #  Runtime: 49ms
        i=0
        temp=''
        ans=''
        while i<len(s):
            temp = temp.strip() + s[i]
            if (s[i]==' ' or i==len(s)-1) and temp!=' ':
                if ans=='':
                    ans=temp.strip()+ans
                    temp=''
                    i+=1
                    continue
                else:
                    ans=temp.strip()+' '+ans
                    temp=''
                    i+=1
                    continue
            i+=1
        return ans
        