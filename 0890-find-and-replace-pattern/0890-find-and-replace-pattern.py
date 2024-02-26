class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # gather letters' occurence in pattern
        d=defaultdict(list)
        for c in range(len(pattern)):
               d[pattern[c]].append(c)
        ans=[]
        for w in words:
            temp=defaultdict(list)
            for l in range(len(w)):
                temp[w[l]].append(l)
                if len(list(temp.values()))>len(list(d.values())):
                    break
            if list(temp.values()) == list(d.values()):
                ans.append(w)
        return ans