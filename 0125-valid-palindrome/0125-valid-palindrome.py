import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Define a regex pattern to match special characters and spaces
        if len(s)==1:
            return True
        if len(s)==0:
            return False

        s=re.sub(r'[^a-zA-Z0-9]','',s.lower())
        return s==s[::-1]
        