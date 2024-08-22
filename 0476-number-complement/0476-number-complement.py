class Solution:
    def findComplement(self, num: int) -> int:
        s=bin(num)
        print(s[2:])
        s1=list(s[2:])
        for c in range(len(s1)):
            # print(c)
            if s1[c]=='1':
                # print(s1[c])
                s1[c] ='0'
                # print(s1[c])
            else:
                s1[c]='1'
        ans="".join(s1)
        print(int(ans,2))
        return int(ans,2)