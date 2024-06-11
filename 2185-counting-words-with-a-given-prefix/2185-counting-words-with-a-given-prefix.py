class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt=0 
        for w in words:
            if w[0]!=pref[0]:
                next
            if w[:len(pref)]==pref:
                cnt+=1
        return cnt