class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count=0
        m=0
        ans=0
        
        for i in range(len(bank)):
            # with these lines, Runtime = 190ms around 25% faster than other esubmissions
            # if '1' not in bank[i]:
            #     continue
            
            for j in range(len(bank[i])):
                if bank[i][j]=='1':
                    m+=1
            if m==0:
                continue
            ans+=count*m
            count=m
            m=0
            
        return ans