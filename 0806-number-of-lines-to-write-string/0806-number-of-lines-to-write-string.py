import string

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        
        lines = 0
        tot = 0
        
        for l in range(len(s)):
            
            ind = string.ascii_lowercase.index(s[l])
            
            if tot + widths[ind] > 100:
                tot = 0
                lines += 1
                tot += widths[ind]
            else:
                tot += widths[ind]
        return [lines + 1, tot]
        # Runtime: 36 ms, faster than 57.89% of Python3 online submissions
#         alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#         lines = 0
#         tot = 0
#         for l in range(len(s)):
            
#             ind = alph.index(s[l])
            
#             if tot + widths[ind] > 100:
#                 tot = 0
#                 lines += 1
#                 tot += widths[ind]
#             else:
#                 tot += widths[ind]
#         return [lines + 1, tot]