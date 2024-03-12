class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans=''
        for i in order:
            if i in s:
                ans+=i
        
        for i in s:
            if i not in ans:
                ans+=i
        print(ans)
        for i in range(len(s)):
            if s.count(ans[i])>ans.count(ans[i]):
                ans = ans[:i] + ans[i] + ans[i:]
        # ans = ans+''.join([char for char in s if s.count(char) > ans.count(char)])
        
        return ans