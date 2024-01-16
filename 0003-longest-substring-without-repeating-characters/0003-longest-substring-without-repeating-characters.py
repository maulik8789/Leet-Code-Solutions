class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(lambda: 0)
        o=''
        o1=''
        isDup=0
        if len(s)==1:
            return 1
        for l in range(len(s)):
            if s[l] not in o:
                o+=s[l]
            elif s[l] in o and len(o)>=len(o1):
                o1=o
                o=o[o.index(s[l])+1:]+s[l]
            elif s[l] in o and len(o)<len(o1):
                o=o[o.index(s[l])+1:]+s[l]
            print('o: o1', o,o1)
        return len(o1) if len(o1)>len(o) else len(o)

#             d[s[l]]+=1
#             if d[s[l]]==2 and len(o)>=len(o1):
#                 isDup=1
#                 o1=o
#                 d=defaultdict(lambda: 0)
#                 d[s[l]]+=1
#                 if s[l]!=s[l-1]:
#                     o=o[o.index(s[l]):]
#                 else:
#                     o=s[l]
#                 print('o: ',o)
#                 print(d)

#             else:
#                 o+=s[l]

#             print(d)
#             print(o)

#         if isDup==0:
#             return len(s)
#         return len(o1) if len(o1)>len(o) else len(o)