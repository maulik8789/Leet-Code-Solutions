class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        rght,lft = len(numbers)-1, 0
        while lft < rght:
            if numbers[lft] + numbers[rght] == target:
                break
            elif numbers[lft] + numbers[rght] > target:
                rght-=1
            else:
                lft+=1
        return [lft+1, rght+1]
            