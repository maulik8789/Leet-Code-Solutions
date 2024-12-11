class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l = len(str1) if len(str1) > len(str2) else len(str2)
        
        # Recursion!
        
        if str1 + str2 != str2 + str1:
            return ""
        elif str1 == str2:
            return str1
        
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])