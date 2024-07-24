class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        st=[]
        for i in range(len(nums)):
            st.append(str(nums[i]))
        arr=[]
        for s in range(len(st)):
            n=''
            n1=''
            for c in range(len(st[s])):
                # print(s,c, int(st[s][c]))
                n+=str(mapping[int(st[s][c])])
                n1+=str(c)
            arr.append(int(n))
        d=defaultdict()
        for i in range(len(nums)):
            d[nums[i]]=arr[i]
        if max(arr)==min(arr):
            return nums
        nums.sort(key=lambda x: (d[x], -x))
        return nums
