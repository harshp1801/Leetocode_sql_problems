class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dct = {}
        for i in nums:
            if i not in dct:
                dct[i] = 1
            else:
                dct[i]+=1
            if dct[i]>len(nums)//2:
                return i
        return - 1
        