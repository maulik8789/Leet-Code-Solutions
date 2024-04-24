class Solution:
    def tribonacci(self, n: int) -> int:
        t=3
        ans=0
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        op=[0,1,1]    
        while t<=n:
            print(sum([op[x] for x in range(len(op)-3,len(op)) ]))
            # sumNum=sum(op[-2],op[-3])
            op.append(sum([op[x] for x in range(len(op)-3,len(op)) ]))
            t+=1
        print(op)
        return op[-1]