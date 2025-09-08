class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        max_p = 0
        while r<len(prices):
            if prices[l]<prices[r]:
                profit = prices[r]-prices[l]
                max_p = max(max_p,profit)
            else:
                l = r # why we want the l as lowest if prices[l]<prices[r] 
                      # simply mean found new price lower than previous
            r+=1
        return max_p


