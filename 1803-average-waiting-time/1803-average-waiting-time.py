class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        c=customers
        t=c[0][0]
        cTime=0
        for i in range(len(c)):
            # if i==0:
            #     t+=c[i][1]
            if t>=c[i][0]:
                t+=c[i][1]
            elif i>0:
                t=c[i][0]+c[i][1]
            cTime+=t-c[i][0]
            print(cTime)
        return cTime/len(c)