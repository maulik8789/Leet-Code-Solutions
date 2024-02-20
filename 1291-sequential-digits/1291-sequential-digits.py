class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        res=[]
        for i in range(1,10):
            num=i
            nextNum=i+1
            
            while num<=high and nextNum<=9:
                num=num*10+nextNum
                if low<=num<=high:
                    res.append(num)
                nextNum+=1
        return sorted(res)
