class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for i in digits:
            s+=str(i)
        num=int(s)+1
        ans=[]
        for c in str(num):
            ans.append(int(c))
        return ans