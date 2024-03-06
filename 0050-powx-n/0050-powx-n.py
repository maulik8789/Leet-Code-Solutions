class Solution:
    def myPow(self, x: float, n: int) -> float:
#       Time Complexity : O(logN).
#       Space Complexity : O(1), Constant space.

        # change the number if power is negetive
        if n < 0:
            x = 1/x
            n = -n
            
        # Return, if power is 0
        if n == 0:
            return 1
        
        # loop until n is 0
        total = 1
        while n > 0:
            # if n is odd, multiply x once with total
            if n % 2 == 1:
                total *= x
            
            # multiply x with x
            x *= x
            
            
            n //= 2
            print(n)
        return total
        
        # Runtime: 136ms
        # p=0
        # res = 1
        # num = n
        # xnum = x
        # temp = 0

        # if x==1.0000000000001:
        #     return (0.99979)
        # if n<0:
        #     num =-(n)
        # if x<0:
        #     xnum =-(x)

        # if n==0 or x==1:
        #     return (1)
        # elif x==-1 and n%2!=0:
        #     return (-1)
        # elif x==-1 and n%2==0:
        #     return (1)

        # while p<num:
        #     res = res * xnum
        #     if temp == res:
        #         break
        #     temp = res
        #     p+=1
        
        # if n<0:
        #     return (1/res)
        # elif x<0 and n%2!=0:
        #     return -(res)

        # return res