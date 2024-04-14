class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxC=max(candies)
        op=[False]*len(candies)
        # op=[]
        # print(op)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=maxC:
                op[i]=True
                # op.append(True)
            # else:
                # op.append(False)
        return op