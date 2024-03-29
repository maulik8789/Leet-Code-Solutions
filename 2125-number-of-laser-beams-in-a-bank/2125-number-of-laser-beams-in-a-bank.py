class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count,m,ans=0,0,0
        
        for i in range(len(bank)):
            
            if '1' not in bank[i]:
                continue
            
            for j in range(len(bank[i])):
                if bank[i][j]=='1':
                    m+=1
            ans+=count*m
            count,m=m,0 
        
        return ans