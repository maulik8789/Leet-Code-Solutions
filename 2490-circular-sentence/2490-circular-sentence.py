class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        a=sentence.split(' ')
        a.append(a[0])
        for i in range(len(a)-1):
            if a[i][-1]!=a[i+1][0]:
                return False
        return True