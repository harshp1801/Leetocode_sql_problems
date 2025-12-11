class Solution(object):
    def twoSum(self, nums, target):
        num_ind = {}
        for i in range(len(nums)):
            temp = target-nums[i]
            if temp in num_ind.keys():
                return [i,num_ind[temp]]
            num_ind[nums[i]] = i
        return None
