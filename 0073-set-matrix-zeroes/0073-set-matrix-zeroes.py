class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        geti=[]
        getj=[]
        zeroIn=[]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    geti.append(i)
                    zeroIn.append(j)
        
        for i in range(len(matrix)):
            if i in geti:
                matrix[i]=[0]*len(matrix[i])
                continue
            for j in range(len(matrix[0])):
                if j in zeroIn:
                    matrix[i][j]=0
