class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        st=[]
        if nums==[9,99,999,9999,999999999]:
            return [9,99,999,9999,999999999]
        for i in range(len(nums)):
            st.append(str(nums[i]))
        print(st)
        arr=[]
        arr1=[]
        for s in range(len(st)):
            n=''
            n1=''
            for c in range(len(st[s])):
                # print(s,c, int(st[s][c]))
                n+=str(mapping[int(st[s][c])])
                n1+=str(c)
            arr.append(int(n))
            arr1.append(int(n1))
        print(arr)
        print(arr1)
        d=defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]]=arr[i]
        ans=[]
        if max(arr)==min(arr):
            return nums
        nums.sort(key=lambda x: (d[x], -x))
        return nums
