class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=0
        while n:
            print('bef ', n)
            n= n & (n-1)
            ans+=1
            print(n)
        return ans