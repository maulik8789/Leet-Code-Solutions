class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d=defaultdict(int)
        ans=[]
        for i in arr:
            d[i]+=1
        for i in arr:
            if d[i]>1:
                next
            else:
                ans.append(i)

        # for i in arr:
        #     d[i]+=1
        #     if d[i]>1:
        #         ans.pop(ans.index(i))
        #     else:
        #         ans.append(i)
        return ans[k-1] if k-1<len(ans) else ''