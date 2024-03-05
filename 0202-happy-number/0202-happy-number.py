class Solution:
    def isHappy(self, n: int) -> bool:
        def tot(num):
            digs=0
            while num>0:
                # print('start',digs, num)
                digs+= (num%10) * (num%10)
                num=int(num/10)
                # print(digs, num)
            return digs
        
        sm=n
        while sm!=1:
            # print(sm)
            sm=tot(sm)
            # print('s',sm)
            if sm==1:
                return True
            if sm==4:
                return False
        return True 