class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[]
        print(ans)
        ans.append([1])
        if rowIndex==0:
            return ans[-1]
        ans.append([1,1])
        if rowIndex==1:
            return ans[-1]
        for i in range(2,rowIndex+2):
            ans.append([])
            ans[i].append(1)
            for j in range(1,i):
                print(i,j, ans)
                ans[i].append(ans[i-1][j-1]+ans[i-1][j])
                print(ans[i])
            ans[i].append(1)
        print(ans)
        return ans[rowIndex]