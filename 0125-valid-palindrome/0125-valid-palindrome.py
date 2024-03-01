class Solution:
    def isPalindrome(self, s: str) -> bool:
        # st=s.replace('','')
        # Define a regex pattern to match special characters and spaces
        sc= set("!@#$%^&*()_+{}[]:;<>,.?/~`\"'- ")
        
        for i in s:
            if i in sc:
                s=s.replace(i,'')
        print(s[::-1])
        return s.lower()==s[::-1].lower()
        