class Solution:
    def frequencySort(self, s: str) -> str:
        freq=defaultdict(int)
        
        # add frequency as value to all letters in the string 
        for l in s:
            freq[l]+=1
        
        # using a bucket
        bucket = [[] for _ in range(len(s)+1)]
        
        # add letters on the index according to their frequency
        for ch, fr in freq.items():
            bucket[fr].append(ch)
            
        estr='' 
        
        # starting from the most frequent letter, go backwards to the lowest
        for i in range(len(bucket)-1,-1,-1):
            if bucket[i]:
                for ch in bucket[i]:
                    estr+=ch*i
        return estr
            