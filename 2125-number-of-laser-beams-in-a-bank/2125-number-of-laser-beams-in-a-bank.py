class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        mul=[]
        count=0
        m=0
        ans=0
        
        for i in range(len(bank)):
            print(i)
            if '1' not in bank[i]:
                # bank.pop(i)
                # i-=1
                continue
            for j in range(len(bank[i])):
                if bank[i][j]=='1':
                    print(i,j)
                    m+=1
                    # if count!=0:
                        # ans+=count+1
            ans+=count*m
            count=m
            m=0
        return ans