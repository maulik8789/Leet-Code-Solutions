import string

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        alph = 'abcdefghijklmnopqrstuvwxyz'
        lines = 0
        tot = 0
        for l in range(len(s)):
            ind = alph.index(s[l])
            
            if tot + widths[ind] > 100:
                tot = 0
                lines += 1
                tot += widths[ind]
            else:
                tot += widths[ind]
        return [lines + 1, tot]