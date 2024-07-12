class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for char in s:
            if char=='*':
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
        # Runtime 3984ms Mem 17.6MB
        # i=0
        # if '*' not in s:
        #     return s
        # while i <len(s):
        #     # print(i, s[i], s)
        #     if s[i]=='*' and i!=len(s)-1:
        #         s=s[:i-1]+s[i+1:]
        #         i-=2
        #         if i<0:
        #             i=0
        #     elif s[i]=='*':
        #         s=s[:i-1]
        #         break
        #     else:
        #         i+=1

        # return s