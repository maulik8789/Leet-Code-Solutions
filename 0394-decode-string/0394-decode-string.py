class Solution:
    def decodeString(self, s: str) -> str:     
        """
        #Runtime: 23 ms, faster than 98.36% of Python3
        # This is an example of Stack
        """
        dig=0
        stck=[['',1]]
        
        for c in s:
            # if character is digit, keep adding numbers
            if c.isdigit():
                dig = dig*10 + int(c)
            
            # if character is an alphabet keep adding in string
            elif c.isalpha():
                stck[-1][0]+=c
                
            # when bracket starts add an empty string and 
            # the dig gathered to stack    
            elif c == '[':
                stck.append(['',dig])
                #empty the digit after it is stored
                dig=0
                # print(stck)
                
            # when the bracket is closed, get last element of Stack which is the string and digit.
            # remove(pop) them from the stack and add the multiplication of that string with digit to 
            # 'new' last string of the Stack

            elif c==']' :
                # print(stck)
                prev_str,prev_dig=stck.pop()
                # print(stck)
                # print(prev_str, prev_dig)
                stck[-1][0]+=(prev_str * prev_dig)
                # print(stck)

        # return the string part from the Stack      
        return stck[0][0]