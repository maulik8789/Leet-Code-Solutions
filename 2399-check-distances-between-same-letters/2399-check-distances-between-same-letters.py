class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d=defaultdict(int)

        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]=i-d[s[i]]-1
            else:
                d[s[i]]=i
        alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
            'q','r','s','t','u','v','w','x','y','z']
        j=0
        print((d.keys()))
        for key in sorted(d.keys()):
            print(d)
            if d[key]!=distance[alp.index(key)]:
                return False
            j+=1
        return True