#Vaatasin kuidas teised on seda ülesannet lahendanud ja sain aru, kuidas peaks tegema.
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_nums = len(nums)
        eelnev = [1] * len_nums
        jargnev = [1] * len_nums
        
        for i in range(1, len_nums):#Loop forwards
            eelnev[i] = eelnev[i-1] * nums[i-1]
        for i in range(len_nums-2, -1, -1):#Loop through backwards
            jargnev[i] = jargnev[i+1] * nums[i+1]
        for i in range(len_nums):
            nums[i] = eelnev[i] * jargnev[i]
        return nums