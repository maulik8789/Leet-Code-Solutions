class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d1=defaultdict(int)
        for i in items1:
            d1[i[0]]+=i[1]
        for i in items2:
            d1[i[0]]+=i[1]
        ans=[]    
        for key,val in d1.items():
            ans.append([key,val])
        return sorted(ans)