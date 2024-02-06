class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ind=[]
        isFrst=0
        for i in range(len(s)):
            if s[i]==c:
                ind.append(i)
        
        ans=[]
        j=0
        for i in range(len(s)):
            if i==ind[j]:
                ans.append(ind[j]-i)
                if len(ind)>1 and j<len(ind)-1:
                    j+=1
                    isFrst=1
            elif isFrst:
                ans.append(min(abs(i-ind[j-1]),abs(ind[j]-i)))
            else:
                ans.append(abs(ind[j]-i))
        return ans
                