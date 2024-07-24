class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        st=[]
        for i in range(len(nums)):
            st.append(str(nums[i]))
        arr=[]
        for s in range(len(st)):
            # n=str(mapping[int(st[s][0])])
            p=mapping[int(st[s][0])]
            for c in range(1,len(st[s])):
                # print(s,c, int(st[s][c]))
                p=p*(10)+mapping[int(st[s][c])]
                # n+=str(mapping[int(st[s][c])])
            arr.append(p)
            # print(arr)
            # print(p)
        d=defaultdict()
        for i in range(len(nums)):
            d[nums[i]]=arr[i]
        if max(arr)==min(arr):
            return nums
        nums.sort(key=lambda x: (d[x], -x))
        return nums
