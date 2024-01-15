class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        o1=''
        o=''
        if len(strs)==1:
            return strs[0]
        l=len(min(strs, key=len))
        for i in range(len(strs)):

            for j in range(l):
                if strs[0][j]==strs[i][j]:
                    o1+=strs[0][j]
                elif strs[0][j]!=strs[i][j]:
                    break
            if o1=='':
                return o1
            if o=='' or o1<=o:
                o=o1
                o1=''
        return o
                
                
                    