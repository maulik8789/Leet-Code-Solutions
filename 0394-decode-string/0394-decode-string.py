class Solution:
    def decodeString(self, s: str) -> str:     
        dig=0
        stck=[['',1]]
        
        for c in s:
            if c.isdigit():
                dig = dig*10 + int(c)
            
            elif c.isalpha():
                stck[-1][0]+=c
                
            elif c == '[':
                stck.append(['',dig])
                dig=0
                # print(stck)
                
            elif c==']' :
                # print(stck)
                prev_str,prev_dig=stck.pop()
                # print(stck)
                # print(prev_str, prev_dig)
                stck[-1][0]+=(prev_str * prev_dig)
                # print(stck)

        return stck[0][0]