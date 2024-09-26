class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s)==0:
            return True
        ind=0
        s1=''
        # Loop through string `t`
        # if current letter `char` is equal to 
        # the current letter[ind] of string `s`,
        # add that letter to string `s1`
        for char in range(len(t)):
            if ind>len(s)-1:
                break
            if s[ind]==t[char]:
                s1+=t[char]
                ind+=1
        
        # check if the strings `s1` and `s` are same
        # return True or False accordingly
        return s1==s