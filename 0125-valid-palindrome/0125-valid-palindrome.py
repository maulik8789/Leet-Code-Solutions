class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Define a regex pattern to match special characters and spaces
        if len(s)==1:
            return True
        if len(s)==0:
            return False
        sc= "!@#$%^&*()_+{}[]:;<>,.?/~`\"'- "
        s=s.lower()
        for i in s:
            if i in sc:
                s=s.replace(i,'')
        return s==s[::-1]
        