class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr=sorted(arr)
        diff=arr[0]-arr[1]
        isFalse=0
        ans=''
        for j in range(2,len(arr)):
            if diff==(arr[j-1]-arr[j]):
                continue
            else:
                return False
                isFalse=1
                break
        if not isFalse:
            return True
        return False