class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d=defaultdict(int)
        ans=[]
        
        for i in nums:
            d[i]+=1
        if len(nums)==1 or (max(d.values())==min(d.values()) and max(d.values())==1):
            return nums
        if k==1:
            return [key for key, value in d.items() if value == max(d.values())]
        
        for i in range(max(d.values()),min(d.values()) - 1,-1):
            
            if k==0:
                break
            for key, value in d.items():
                if value == i:
                    ans.append(key)
                    k-=1

        return ans