class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sArray(num):
            lenNum=len(num)
            if len(num)>1:
                
                lArr=num[:lenNum//2]
                rArr=num[lenNum//2:]

                #recursion
                sArray(lArr)
                sArray(rArr)

                i,j,k=0,0,0

                while i<len(lArr) and j<len(rArr):
                    if lArr[i]<rArr[j]:
                        num[k]=lArr[i]
                        i+=1
                    else:
                        num[k]=rArr[j]
                        j+=1
                    k+=1

                while i<len(lArr):
                    num[k]=lArr[i]
                    i+=1
                    k+=1
                while j<len(rArr):
                    num[k]=rArr[j]
                    j+=1
                    k+=1
                
            return num
        
        return sArray(nums)






























        # def sArray(num):
        #     if len(num)>1:
        #         left_arr=num[:len(num)//2]
        #         right_arr=num[len(num)//2:]

        #         # recursion
        #         sArray(left_arr)
        #         sArray(right_arr)

        #         # merge
        #         i,j,k=0,0,0

        #         while i < len(left_arr) and j < len(right_arr):
        #             if left_arr[i]<right_arr[j]:
        #                 num[k]=left_arr[i]
        #                 i+=1
        #             elif right_arr[j]<=left_arr[i]:
        #                 num[k]=right_arr[j]
        #                 j+=1
        #             k+=1

        #         while i<len(left_arr):
        #                 num[k]=left_arr[i]
        #                 i+=1
        #                 k+=1
        #         while j<len(right_arr):
        #                 num[k]=right_arr[j]
        #                 j+=1
        #                 k+=1
                    
        #     return num
        # return sArray(nums)
                    