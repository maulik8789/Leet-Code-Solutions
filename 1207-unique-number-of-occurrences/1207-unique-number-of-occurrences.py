class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=defaultdict(int)
        for i in range(len(arr)):
            d[arr[i]]=d[arr[i]]+1
        s=set((d.values()))
        if len(s)==len(list(d.values())):
            return True
        else:
            return False