class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        def merge_sort(arr):
            if len(arr)>1:
                nums01=arr[:len(arr)//2]
                nums02=arr[len(arr)//2:]

                # recursion
                merge_sort(nums01)            
                merge_sort(nums02)

                # merge
                i=0
                j=0
                k=0
                
                while i<len(nums01) and j<len(nums02):
                    if nums01[i]<nums02[j]:
                        arr[k]=nums01[i]
                        i+=1
                    elif nums02[j]<=nums01[i]:
                        arr[k]=nums02[j]
                        j+=1
                    k+=1

                while i<len(nums01):
                    arr[k]=nums01[i]
                    i+=1
                    k+=1
                while j<len(nums02):
                    arr[k]=nums02[j]
                    j+=1
                    k+=1
            return arr
        l=merge_sort(nums1[:m]+nums2[:n])
        nums1.clear()
        nums1.extend(l)