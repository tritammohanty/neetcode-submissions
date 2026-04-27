class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = [0]
        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    diff.append(prices[j]-prices[i])

        return max(diff) 
