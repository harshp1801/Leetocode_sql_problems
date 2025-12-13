class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = float('inf')
        curr_max = float('-inf')
        diff = []
        for i in prices:
            if i<curr_min:
                curr_min = i
                curr_max = 0
            elif i>curr_max:
                curr_max = i
            if curr_min<curr_max:
                diff.append(curr_max-curr_min)
            else:
                diff.append(0)
        return max(diff)
        