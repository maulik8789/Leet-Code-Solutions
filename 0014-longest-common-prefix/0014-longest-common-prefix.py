class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        o1=''
        o2=''
        o=''
        if len(strs)==1:
            return strs[0]
        for i in range(len(strs)):
            if len(strs[0])>=len(strs[i]):
                l=len(strs[i])
            else:
                l = len(strs[0])

            for j in range(l):
                if strs[0][j]==strs[i][j]:
                    o1+=strs[0][j]
                elif strs[0][j]!=strs[i][j]:
                    break
            if o1=='':
                return o1
            if o=='':
                o=o1
                o1=''
            elif o1<=o:
                o=o1
                o1=''
            print(o1)
        return o
                
                
                    