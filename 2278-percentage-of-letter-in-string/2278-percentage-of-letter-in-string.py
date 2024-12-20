class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        ans = 0
        for l in s:
            if l == letter:
                ans += 1
        return math.floor(ans / len(s) * 100)