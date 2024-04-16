class Solution:
    def addDigits(self, num: int) -> int:
        print(str(num))
        s=str(num)
        ans=0
        while len(s)>1:
            for i in s:
                ans+=int(i)
            s=str(ans)
            print(s)
            ans=0
        return int(s)