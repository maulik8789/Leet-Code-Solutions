class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n==1 or n==0:
            return n
        ans=[0]*(n)
        i=0
        x=1
        c=0
        while c<n-1:
            # print(ans)
            if i==len(ans):
                i=0
            if x==k and ans[i] == 0:
                ans[i]=1
                c+=1
                x=1
            elif ans[i]==0:
                x+=1
            i+=1
            # print(i, x)
            
            # print(ans)
            # if c==len(ans)-1:
            #     break
        return (ans.index(0))+1
        # 'for l in range(len(ans)):
        #     if ans[l]==0:
        #         return l+1
        # return 100'