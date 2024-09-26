class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]
        
        for b in s:
            # add ONLY start of the brackets
            if b in '{[(':
                stack.append(b)
            else:
                # if the any beginning of a bracket 
                # is not one of '{[(', return False
                if not stack:
                    return False
                
                # keep removing one start of last brackets from stack
                if ((b==')' and stack[-1]=='(') \
                    or (b==']' and stack[-1]=='[') \
                    or (b=='}' and stack[-1]=='{')) and stack[-1]:
                    stack.pop(-1)
                # If the current 'b' is end of a bracket and there is no start
                # of that bracket in stack,
                # then, return False
                else:
                    return False
        # return True if there is nothing left in Stack
        # return False if there is any bracket left in Stack
        return not stack
                    
                    