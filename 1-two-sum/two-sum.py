class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dct = {}
        for i in range(len(nums)):
            sub = target-nums[i]
            if nums[i] in dct.keys():
                return [dct.get(nums[i]),i]
            dct[sub] = i
            