class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Define a regex pattern to match special characters and spaces
        sc= "!@#$%^&*()_+{}[]:;<>,.?/~`\"'- "
        
        for i in s:
            if i in sc:
                s=s.replace(i,'')
        return s.lower()==s[::-1].lower()
        