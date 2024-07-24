class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        st=[]
        for i in range(len(nums)):
            st.append(str(nums[i]))

        d=defaultdict()

        for s in range(len(st)):
            p=mapping[int(st[s][0])]
            for c in range(1,len(st[s])):
                p=p*(10)+mapping[int(st[s][c])]
            d[int(st[s])]=p

        if max(d.values())==min(d.values()):
            return nums

        nums.sort(key=lambda x: (d[x], -x))
        return nums







        # st=[]
        # for i in range(len(nums)):
        #     st.append(str(nums[i]))

        # # arr=[]
        # d=defaultdict()

        # for s in range(len(st)):
        #     # n=str(mapping[int(st[s][0])])
        #     p=mapping[int(st[s][0])]
        #     for c in range(1,len(st[s])):
        #         # print(s,c, int(st[s][c]))
        #         p=p*(10)+mapping[int(st[s][c])]
        #         # n+=str(mapping[int(st[s][c])])
        #     # arr.append(p)
        #     d[int(st[s])]=p
        #     # print(arr)
        #     # print(p)
        # # for i in range(len(nums)):
        #     # d[nums[i]]=arr[i]
        # if max(d.values())==min(d.values()):
        #     return nums
        # nums.sort(key=lambda x: (d[x], -x))
        # return nums
