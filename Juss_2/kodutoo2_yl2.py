class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries: # kui timeSeries on tühi, siis tagasta 0
            return 0 
        total = 0 # loome muutuja total, mis on alguses 0
        for i in range(1, len(timeSeries)): # tsükkel, mis käib läbi timeSeries listi elemendid alates teisest elemendist kuni viimase elemendini
            total += min(timeSeries[i] - timeSeries[i - 1], duration) # leia miinimumi väärtus kahe elemendi vahel ja liida see total muutujale
        return total + duration # tagasta terve aeg, mis ajal on Ashe mürgitatud