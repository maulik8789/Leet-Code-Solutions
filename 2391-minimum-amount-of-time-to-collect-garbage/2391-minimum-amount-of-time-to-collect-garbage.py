class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        colM,colP,colG=0,0,0
        lstM,lstP,lstG=0,0,0
        
        tr=0
        ans=0
        for i in range(len(garbage)-1,-1,-1):
            if 'P' in garbage[i] and lstP==0:
                lstP=i
            if 'G' in garbage[i] and lstG==0:
                lstG=i
            if 'M' in garbage[i] and lstM==0:
                lstM=i
            
            print(lstP,lstG,lstM)
        for j in range(3):
            for i in range(len(garbage)):
                if tr==0:
                    l='P'
                    lst=lstP
                elif tr==1:
                    l='G'
                    lst=lstG
                elif tr==2:
                    l='M'
                    lst=lstM
                if l in garbage[i]:
                    for c in garbage[i]:
                        if c==l:
                            colP+=1
                if i>0 and lst>=i:        
                    colP+=travel[i-1]
                print(colP)
            tr+=1
        print(colP)
        return colP