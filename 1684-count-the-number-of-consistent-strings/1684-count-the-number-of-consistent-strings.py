class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans=0
        for word in words:
            notAllowed=0
            for c in word:
                if c not in allowed:
                    notAllowed=1
                    break
            if not notAllowed:
                ans+=1
        return ans