class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans=[]
        print(ans)
        ans.append([1])
        if numRows==1:
            return ans
        ans.append([1,1])
        if numRows==2:
            return ans
        for i in range(2,numRows):
            ans.append([])
            ans[i].append(1)
            for j in range(1,i):
                print(i,j, ans)
                ans[i].append(ans[i-1][j-1]+ans[i-1][j])
                print(ans[i])
            ans[i].append(1)
        print(ans)
        return ans