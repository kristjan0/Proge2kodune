class Solution:
    def lengthOfLastWord(self, s: str) -> int: #teen funktsioon rawr
        return len(s.split()[-1]) #returnib viimase sõna ja splitib selle ehk eemaldab spaceid sõnade vahelt ja len loendab arvu ez no sweat