class Solution:
    def checkString(self, s: str) -> bool:
        isB=0
        for char in s:
            if char=='a' and isB==1:
                return False
            elif char=='b' and isB==0:
                isB=1
        return True