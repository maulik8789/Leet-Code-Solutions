class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        l=len(original)
        if n*m<l or n*m>l:
            return []
        ans=[[]]
        i=0
        c=0
        ansInd=0
        while i<l:
            if c<n:
                ans[ansInd].append(original[i])
                c+=1
            else:
                ansInd+=1
                ans.append([])
                ans[ansInd].append(original[i])
                c=1
            i+=1
        return ans