class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 0 #panen kirja muutuja algab 0
        for x in nums: #loopiga vaatab koik yle
            i^=x #xor ehk kui on samad siis result 0 ja kui erinev result 1 vmidagi
        return i #tagastab numbri mis ainuke listis