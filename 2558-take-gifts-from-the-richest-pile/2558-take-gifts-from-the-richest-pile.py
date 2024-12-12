import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        tot = 0
        # gifts.sort()
        # gifts = gifts[::-1]
        d = defaultdict(int)
        
        while k > 0:
            k-=1
            # for i in gifts:

            gifts.sort()
            gifts = gifts[::-1]
            # print(gifts)
            sqRoot = math.floor(math.sqrt(gifts[0]))
            # if sqRoot not in gifts:
            gft = sqRoot
            gifts[0] = gft
            # else:
            #     gft = gifts[0]
            #     gifts.pop(0)
            
            d[gft] += 1
            # print(gft)
            
            # tot = tot + gft 
        return sum(gifts)