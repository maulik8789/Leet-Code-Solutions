class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        ans1,ans2='',''
        # ans2=''
        for i in word1:
            ans1+=i
        for i in word2:
            ans2+=i
        return ans1==ans2