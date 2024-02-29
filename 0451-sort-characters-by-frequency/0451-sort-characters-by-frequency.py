class Solution:
    def frequencySort(self, s: str) -> str:
        freq=defaultdict(int)
        for l in s:
            freq[l]+=1
        
        bucket = [[] for _ in range(len(s)+1)]
        
        for ch, fr in freq.items():
            bucket[fr].append(ch)
            
        estr='' 
        
        for i in range(len(bucket)-1,-1,-1):
            if bucket[i]:
                for ch in bucket[i]:
                    estr+=ch*i
        return estr
            