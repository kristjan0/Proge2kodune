class Solution:
    # @param haystack, string
    # @param needle, string
    # @return integer
    def strStr(self, haystack, needle):
        if haystack == needle == '':
            return 0

        n = len(needle) #noela pikkus
        
        for i in range(len(haystack) - n + 1):
            if haystack[i:i+n] == needle: # [i:i+n] indeks i kuni indeks i+n 
                return i

        return -1 #juhul kui polegi haystackis