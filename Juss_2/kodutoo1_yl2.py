#Input: digits = [1,2,3]
#Output: [1,2,4]

class Solution(object): #klassi loomine
    def plusOne(self, numbrid): #funktsiooni loomine
        for i in range(len(numbrid)-1, -1, -1): #tsükkel numbridest tagurpidi läbi käimiseks
            if numbrid[i] < 9: #kui number on väiksem kui 9
                numbrid[i] += 1 #siis liidetakse 1
                return numbrid #tagastatakse number
            else: 
                numbrid[i] = 0 #kui number on suurem kui 9, siis muudetakse number 0-ks
        numbrid.insert(0, 1) #lisatakse number 1
        return numbrid #tagastatakse number