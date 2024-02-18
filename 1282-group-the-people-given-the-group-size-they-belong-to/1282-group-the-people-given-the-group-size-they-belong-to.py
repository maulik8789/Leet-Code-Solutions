class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        fr=defaultdict(list)
        ans=[]
        for ind, i in enumerate(groupSizes):
            fr[i].append(ind)
            if len(fr[i])==i:
                ans.append(fr.pop(i))
        return ans
