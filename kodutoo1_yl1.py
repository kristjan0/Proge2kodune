#nums = [2, 7, 11, 15]
#target = 9

class Solution(object): #teeme klassi
    def twoSum(self, nums, target): #teeme funktsiooni
        for x in range(len(nums)): #teeme for loopi, et saada kõikide numbrite paare
            for y in range(x+1, len(nums)): #teeme teise for loopi, et saada kõikide numbrite paare
                if nums[x] + nums[y] == target: #kui kahe numbri summa on võrdne targetiga
                    return [x, y] #tagastame nende numbrite indeksid