class Solution(object):
    def maximum69Number (self, num):
        num = str(num)
        num = list(num)
        for i in range(len(num)):
            if num[i] == '6':
                num[i] = '9'
                break
        num = ''.join(num)
        return int(num)