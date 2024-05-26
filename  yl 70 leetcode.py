class Solution(object):
    def climbStairs(self, n):
        opt = [0] * (n+1)
       
        if n >= 1:
            opt[1] = 1
        if n >= 2:
            opt[2] = 2

        for i in range(3,n+1):
            opt[i] = opt[i-1] + opt[i-2]
            
        return opt[n]


            
