class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        arr=[]
        for i in range(len(matrix)):
            print(min(matrix[i]))
            print(matrix[i].index(min(matrix[i])))
            arr.append(matrix[i].index(min(matrix[i])))
        print(arr)
        ans=[]
        c=0
        for j in range(len(arr)):
            for i in range(len(matrix)):
                print(matrix[i][arr[j]])
                if matrix[j][arr[j]]>matrix[i][arr[j]]:
                    c+=1
            if c==len(arr)-1:
                return [matrix[j][arr[j]]]
            c=0

        return []