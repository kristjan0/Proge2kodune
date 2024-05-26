#219. Contains Duplicate II

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numsMap = {}
        for i in range(len(nums)):
            if nums[i] in numsMap and i - numsMap[nums[i]] <= k: 
                    return True
            else:
                numsMap[nums[i]] = i
        return False