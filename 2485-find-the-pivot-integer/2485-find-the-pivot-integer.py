class Solution:
    def pivotInteger(self, n: int) -> int:
        tot=0
        for i in range(1,n+1):
            tot=0
            
            for k in range(1,i+1):
                tot+=k
                # print('k',k)
            tot1=0
            for j in range(i,n+1):
                tot1+=j
                # print('j',j)
            if tot==tot1:
                return i
        return -1