class Solution:
    def romanToInt(self, s: str) -> int:
        char = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n=0
        for i in range(len(s)):
            if (i<len(s)-1 and char[s[i]]<char[s[i+1]]):
                n-=char[s[i]]
            else:
                n+=char[s[i]]
        return n