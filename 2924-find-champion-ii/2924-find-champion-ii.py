class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        d=defaultdict(int)
        if len(edges)==0: 
            if n==1:
                return 0
            elif n>1:
                return -1
        for i in range(len(edges)):
            for j in range(len(edges[i])):
                # print(j, d[edges[i][j]])
                if d[edges[i][j]]<=j:
                    d[edges[i][j]]=j
                # print('after ',j, d[edges[i][j]])
        if len(d.keys())<n:
            return -1
        # print(min(d.values()))
        # print(d.items())
        # print([key for key, val in d.items() if val==min(d.values())])                
        champ=[key for key, val in d.items() if val==min(d.values())]                
        return champ[0] if len(champ)==1 else -1
