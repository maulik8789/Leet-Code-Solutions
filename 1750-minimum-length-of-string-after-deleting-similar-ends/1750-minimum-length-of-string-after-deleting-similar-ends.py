class Solution:
    def minimumLength(self, s: str) -> int:
        r=0
        l=len(s)
        # print(r,l)
        while l-r>1 and s[r]==s[l-1]:
            # print(r,l)
            if s[r]==s[l-1]:
                while s[r]==s[l-1] and l-r>1:
                    # print(r,l-1)
                    if s[r]==s[l-1-1]:
                        l-=1
                    elif s[r+1]==s[l-1]:
                        r+=1
                    else:
                        break
                r+=1
                l-=1
            else:
                break
        return l-r if l-r>0 else 0
                