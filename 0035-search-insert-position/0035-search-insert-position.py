class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target>nums[-1]:
            return len(nums)
        for i in nums:
            if i==target or i>target:
                return nums.index(i)