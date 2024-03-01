class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            l=len(words[i])
            left_l=0
            right_l=len(words[i])-1
            isPal=0
            while l>=1:
                
                if words[i][left_l]!=words[i][right_l]:
                    break
                else:
                    left_l+=1
                    right_l-=1
                    l-=2
            if l<=1:
                return words[i]
        return ''