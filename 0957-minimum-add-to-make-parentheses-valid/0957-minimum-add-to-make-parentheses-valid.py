class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for i in s:
            if stack and stack[-1]=='(':
                if i==')':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return len(stack) 
        # d=defaultdict(int)
        # d={
        #     '(':0,
        #     ')':0
        # }
        # for i in s:
        #     d[i]+=1
        # return abs(d['(']-d[')'])