class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def rmv_scr(s,frst,scnd,pnt_val):
            stack=[]
            points=0
            for char in s:
                if stack and stack[-1] == frst and char == scnd:
                    stack.pop()
                    points +=pnt_val
                else:
                    stack.append(char)
            remaining = ''.join(stack)
            return remaining,points


        # Determine the order based on the points
        if x >= y:
            s, points = rmv_scr(s, 'a', 'b', x)
            s, additional_points = rmv_scr(s, 'b', 'a', y)
            points += additional_points
        else:
            s, points = rmv_scr(s, 'b', 'a', y)
            s, additional_points = rmv_scr(s, 'a', 'b', x)
            points += additional_points
        
        return points    