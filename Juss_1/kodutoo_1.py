class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        length = len(nums)
        result = []
        for i in range(length):
            count = 0
            for j in range(length):
                if nums[j] < nums[i]:
                    count += 1
            result.append(count)
        return result