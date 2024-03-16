class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        ans=[]
        for i in range(len(words)):
            evn=''
            odd=''
            for j in range(len(words[i])):
                if j%2==0:
                    evn+= words[i][j]
                else:
                    odd+= words[i][j]
            s=sorted(evn)+sorted(odd)
            ans.append(''.join(s))
        return len(Counter(ans))