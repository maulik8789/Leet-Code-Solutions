class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i in range(len(prices)):
            isDisc = 0
            for j in range(i + 1,len(prices)):
                if prices[j] <= prices[i]:
                    isDisc = 1
                    ans.append(prices[i] - prices[j])
                    break
            if isDisc == 0:
                ans.append(prices[i])
        return ans