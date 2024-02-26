class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        d=defaultdict(list)
        for c in range(len(pattern)):
               d[pattern[c]].append(c)
        ans=[]
        for w in words:
            temp=defaultdict(list)
            for l in range(len(w)):
                temp[w[l]].append(l)
            if list(temp.values()) == list(d.values()):
                ans.append(w)
        return ans
                