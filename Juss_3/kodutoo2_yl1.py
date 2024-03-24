class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0 # i on indeks ja algab 0-st
        while i < len(nums)-1: # kui i on väiksem kui listi pikkus - 1
            if nums[i] == nums[i+1]: # kui listi i ja i+1 on võrdsed
                nums.pop(i) # siis eemalda listist i
            else: 
                i += 1 # kui i ja i+1 ei ole võrdsed, siis liigu järgmisele indeksile
        return len(nums) 