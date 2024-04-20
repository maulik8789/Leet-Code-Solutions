class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d=defaultdict(set)
        for i in range(len(logs)):
            d[logs[i][0]].add(logs[i][1])
        # print(d)
        op=[0]*k
        for i in d.values():
            op[len(i)-1]+=1
        return op
        