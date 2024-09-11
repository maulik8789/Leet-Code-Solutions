class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        This is an example of Dynamic Programming.
        Runtime
        """
        
        if len(s)<2:
            return False
        
        # if 1st char of repeated string is 
        # the 1st char of given string `s`,
        
        # then the last char of repeated string will be
        # the last char of given string `s`
        
        str2=s+s
        
        # if we remove 1st char from 1st repeatition 
        # and we remove last char from last repeptition
        # we still MUST have repeated string in `str2=s+s`
        str2=str2[1:-1]
        return s in str2