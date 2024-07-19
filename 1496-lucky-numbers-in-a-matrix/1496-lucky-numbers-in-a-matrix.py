class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        arr=[]
        for i in range(len(matrix)):
            arr.append(matrix[i].index(min(matrix[i])))
        c=0
        for j in range(len(arr)):
            for i in range(len(matrix)):
                if matrix[j][arr[j]]>matrix[i][arr[j]]:
                    c+=1
            if c==len(arr)-1:
                return [matrix[j][arr[j]]]
            c=0
        return []