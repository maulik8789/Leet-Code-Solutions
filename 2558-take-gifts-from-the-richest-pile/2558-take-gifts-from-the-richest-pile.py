import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        tot = 0
        d = defaultdict(int)
        
        while k > 0:
            k-=1
            gifts.sort(reverse = True)
            # gifts = gifts[::-1]
            sqRoot = math.floor(math.sqrt(gifts[0]))
            gft = sqRoot
            gifts[0] = gft

        return sum(gifts)