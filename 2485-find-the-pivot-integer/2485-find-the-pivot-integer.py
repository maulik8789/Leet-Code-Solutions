class Solution:
    def pivotInteger(self, n: int) -> int:
        right_sum=n*(n+1)//2
        left_sum=0
        for i in range(1,n+1):
            right_sum-=i
            if right_sum==left_sum:
                return i
            left_sum+=i
        return -1
        # # Runtime: 2017 ms, faster than 5.08% of Python3
        # tot=0
        # for i in range(1,n+1):
        #     tot=0
        #     for k in range(1,i+1):
        #         tot+=k
        #     tot1=0
        #     for j in range(i,n+1):
        #         tot1+=j
        #     if tot==tot1:
        #         return i
        # return -1