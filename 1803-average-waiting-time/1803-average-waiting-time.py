class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        c=customers
        l=len(customers)
        t=c[0][0]
        cTime=0
        for i in range(l):
            # if i==0:
            #     t+=c[i][1]
            if t>=customers[i][0]:
                t+=customers[i][1]
            elif i>0:
                t=customers[i][0]+customers[i][1]
            cTime+=t-customers[i][0]
            # print(cTime)
        return cTime/l