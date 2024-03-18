class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        tot=0
        for s in stones:
            if s in jewels:
                tot+=1
        return tot