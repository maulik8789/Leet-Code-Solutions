class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target)!=len(arr) or set(target)!=set(arr):
            return False
        dA=defaultdict(int)
        dT=defaultdict(int)
        for i in range(len(arr)):
            dA[arr[i]]+=1
            dT[target[i]]+=1
        # for i in range(len(target)):
        #     dT[target[i]]+=1
        for key, val in dA.items():
            if dA[key]!=dT[key]:
                return False
        return True
