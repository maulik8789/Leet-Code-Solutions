class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in arr:
            if i == 0:
                if len([i for i, val in enumerate(arr) if val == 0]) > 1:
                    return True
                else: continue
            if 2*i in arr:
                return True
        return False
            