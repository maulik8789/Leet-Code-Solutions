class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        getRow=len(matrix)
        getCol=len(matrix[0])
        geti=[]
        getj=[]
        zeroIn=[]

        for i in range(getRow):
            for j in range(getCol):
                if matrix[i][j]==0:
                    geti.append(i)
                    zeroIn.append(j)
        
        for i in range(getRow):
            if i in geti:
                matrix[i]=[0]*len(matrix[i])
                continue
            for j in range(getCol):
                if j in zeroIn:
                    matrix[i][j]=0
