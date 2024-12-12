import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Use heap for better Runtime
        while k > 0:
            k-=1
            gifts.sort(reverse = True)
            sqRoot = math.floor(math.sqrt(gifts[0]))
            gifts[0] = sqRoot

        return sum(gifts)