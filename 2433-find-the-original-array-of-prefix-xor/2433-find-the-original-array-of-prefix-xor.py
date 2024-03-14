import math
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans=[pref[0]]
        for i in range(1,len(pref)):
            ans.append(pref[i-1]^pref[i])
        return ans
        # exponent = math.log(result, base)
        # Time limit Execeeded
        # ans=[pref[0]]
        # for i in range(1,len(pref)):
        #     exponent = 1
        #     while pref[i-1] ^ exponent != pref[i]:
        #         exponent += 1
        #     ans.append(exponent)
        # return ans
    