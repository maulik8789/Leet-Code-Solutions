class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        d={
            'A':1,
            'B':2,
            'C':3,
            'D':4,
            'E':5,
            'F':6,
            'G':7,
            'H':8,
            'I':9,
            'J':10,
            'K':11,
            'L':12,
            'M':13,
            'N':14,
            'O':15,
            'P':16,
            'Q':17,
            'R':18,
            'S':19,
            'T':20,
            'U':21,
            'V':22,
            'W':23,
            'X':24,
            'Y':25,
            'Z':26
        }
        ans=0
        l=len(columnTitle)-1
        for c in range(l,-1,-1):
            ans+=(d[columnTitle[c]]*(26**(l-c)))
        return ans    