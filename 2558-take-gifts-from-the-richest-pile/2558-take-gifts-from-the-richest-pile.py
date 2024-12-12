import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k > 0:
            k-=1
            gifts.sort(reverse = True)
            sqRoot = math.floor(math.sqrt(gifts[0]))
            # gft = sqRoot
            gifts[0] = sqRoot

        return sum(gifts)