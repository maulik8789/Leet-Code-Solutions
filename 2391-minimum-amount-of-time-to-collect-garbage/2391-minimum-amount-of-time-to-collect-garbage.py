class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        colP=0
        lstM,lstP,lstG=0,0,0
        tr=0
        for i in range(len(garbage)-1,-1,-1):
            if 'P' in garbage[i] and lstP==0:
                lstP=i
            if 'G' in garbage[i] and lstG==0:
                lstG=i
            if 'M' in garbage[i] and lstM==0:
                lstM=i
            
        for j in range(3):
            if tr==0:
                    l='P'
                    lst=lstP
            elif tr==1:
                l='G'
                lst=lstG
            elif tr==2:
                l='M'
                lst=lstM
            for i in range(len(garbage)):
                
                if l in garbage[i]:
                    for c in garbage[i]:
                        if c==l:
                            colP+=1
                if i>0 and lst>=i:        
                    colP+=travel[i-1]
            tr+=1
        return colP