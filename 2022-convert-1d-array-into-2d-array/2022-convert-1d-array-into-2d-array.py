class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if n*m<len(original) or n*m>len(original):
            return []
        ans=[[]]
        i=0
        c=0
        ansInd=0
        while i<len(original):
            if c<n:
                ans[ansInd].append(original[i])
                c+=1
            else:
                c=0
                ansInd+=1
                ans.append([])
                ans[ansInd].append(original[i])
                c+=1
            i+=1
        return ans