class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ind=[]
        isFrst=0
        for i in range(len(s)):
            if s[i]==c:
                ind.append(i)
        print(ind)
        
        ans=[]
        j=0
        for i in range(len(s)):
            # print(ind[j])
            # print(ans)
            # print(j)
            if i==ind[j]:
                ans.append(ind[j]-i)
                if len(ind)>1 and j<len(ind)-1:
                    j+=1
                    isFrst=1
            elif isFrst:
                print(ind[j-1], ind[j-1])
                ans.append(min(abs(i-ind[j-1]),abs(ind[j]-i)))
            else:
                ans.append(abs(ind[j]-i))
        print(ans)
        return ans
                