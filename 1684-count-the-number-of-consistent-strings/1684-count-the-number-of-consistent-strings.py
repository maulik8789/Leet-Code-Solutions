class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans=0
        for word in words:
            isAllowed=1
            for c in word:
                if c not in allowed:
                    isAllowed=0
                    break
            if isAllowed:
                ans+=1
        return ans