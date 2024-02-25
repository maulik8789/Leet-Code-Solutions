class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans=[]
        for i in range(len(A)):
            cm=0
            for k in range(i+1):
                for j in range(i+1):
                    # print(i, j, B[:j+1])
                    if A[k] == B[j]:
                        cm+=1
            ans.append(cm)
        return (ans)