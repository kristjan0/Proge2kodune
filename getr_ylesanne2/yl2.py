class Solution:
    def strStr(self, haystack: str, needle: str) -> int: #pmst võtab kaks asja haystack ja needle
        
        if needle in haystack: #otsid needlet haystackist
            return haystack.index(needle) #returnib kui leiab sõna teisest sõnast
        else:
            return -1 #kui ei leia siis annab -1