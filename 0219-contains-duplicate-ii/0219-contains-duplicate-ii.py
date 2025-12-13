class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dct = {}
        for i in range(len(nums)):
            if nums[i] in dct and i - dct[nums[i]]<=k:
                return True    
            dct[nums[i]] = i
        return False
