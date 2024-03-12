class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans=''
        for i in order:
            if i in s:
                ans+=i
        
        # for i in s:
            
        for i in range(len(s)):
            if s[i] not in ans:
                ans+=s[i]
            if s.count(ans[i])>ans.count(ans[i]):
                ans = ans[:i] + ans[i] + ans[i:]
        
        return ans