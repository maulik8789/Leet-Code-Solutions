class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l= len(matrix)
        temp =deepcopy(matrix) 
        print('1st temp: ',temp)
        i = l - 1
        while i>=0:
            if i>l:
                break
            print ('i is:',i)
            j=0
            while j<l:
                print('matrix: ',matrix)
                print('i and j ',i,' ',j)
                print('num ',matrix[i][j])
                num= matrix[i][j]
                temp[j][l-1-i] = num
                print('temp: ',temp)
                j+=1
            i-=1
        print('temp: ',temp)
        matrix.clear()
        matrix.extend(temp) 