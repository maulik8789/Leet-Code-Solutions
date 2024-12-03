class Solution:
    def isHappy(self, n: int) -> bool:
        sq=0
        prev = []
        s=str(n)
        while sq != 1:
            for l in s:
                sq += int(l) ** 2
                # print (l, sq)
            if sq not in prev:
                prev.append(sq)
                s = str(sq)
                sq = 0
            else:
                break
            # print(s, sq, prev)
        return True if sq == 1 else False