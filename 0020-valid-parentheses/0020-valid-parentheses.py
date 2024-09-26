class Solution:
    def isValid(self, s: str) -> bool:
        stackS=[]
        stackC=[]
        stackQ=[]
        stack=[]
        
        for b in s:
            if b in '{[(':
                stack.append(b)
            else:
                if not stack:
                    return False
                if ((b==')' and stack[-1]=='(') \
                    or (b==']' and stack[-1]=='[') \
                    or (b=='}' and stack[-1]=='{')) and stack[-1]:
                    stack.pop(-1)
                else:
                    return False
        return not stack
                    
                    