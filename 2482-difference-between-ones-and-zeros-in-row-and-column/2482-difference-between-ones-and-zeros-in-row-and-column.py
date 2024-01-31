class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        diff=[]
        d=defaultdict(int)
        oneRowKey='oneRow'
        oneColKey='oneCol'
        zeroRowKey='zeroRow'
        zeroColKey='zeroCol'
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    d[f'{oneColKey}{j}']+=1
                    d[f'{oneRowKey}{i}']+=1
                else:
                    d[f'{zeroRowKey}{i}']+=1
                    d[f'{zeroColKey}{j}']+=1
            
        for i in range(len(grid)):
            diff.append([])
            for j in range(len(grid[i])):
                diff[i].append(d[f'{oneRowKey}{i}'] + d[f'{oneColKey}{j}'] - d[f'{zeroRowKey}{i}'] - d[f'{zeroColKey}{j}'] ) 
        return diff