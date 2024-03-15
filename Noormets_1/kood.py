class Solution(object): #O(n^2), O(n) ei osanud teha
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_nums = len(nums) # Set the length of the list so it doesnt have to be calculated every time
        if len_nums < 2  or len_nums > 100000: # Check if the length of the list is within the limits
            return
        answer = [] # Create a list for the answer
        for i in range(len_nums): # Loop through the list
            if nums[i] < -30 or nums[i] > 30: # Check if the number is within the limits
                print(nums[i])
                return
            temp_nums = nums[:i] + nums[i+1:] # Create a temporary list without the current number
            #print(temp_nums) #DEBUG
            answer_nr = 1
            for x in temp_nums: #Loop through temp_nums and multiply the numbers
                answer_nr *= x
            answer.append(answer_nr)
        return answer
        