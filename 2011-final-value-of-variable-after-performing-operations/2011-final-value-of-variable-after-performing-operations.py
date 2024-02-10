class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans=0
        for s in range(len(operations)):
            if '+' in operations[s]:
                ans+=1
            else:
                ans-=1
        return ans