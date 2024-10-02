class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumpLife=0
        
        for i in nums:
            if jumpLife < 0:
                return False
            elif i > jumpLife:
                jumpLife=i
            jumpLife-=1
        return True