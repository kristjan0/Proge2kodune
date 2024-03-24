class Solution():
    def romanToInt(self, s):
       
        # määran rooma numbrimärkide väärtused, essa string teine int
        rooma_vaartused = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

       
        tulemus = 0
        
        eelnev_vaartus = 0

        # lähen läbi iga rooma numbrimärgi jadas
        for rooma in s:
            # leian praeguse märgi väärtuse
            praegune_vaartus = rooma_vaartused[rooma]

            # kui praegune väärtus on suurem kui eelnev siis lahutan eelneva väärtuse kahekordselt
            if praegune_vaartus > eelnev_vaartus:
                tulemus += praegune_vaartus - 2 * eelnev_vaartus
            else:
                tulemus += praegune_vaartus
            
            # uuendan eelneva väärtuse uueks praeguseks väärtuseks 
            eelnev_vaartus = praegune_vaartus

        
        return tulemus

solution = Solution()
print(solution.romanToInt("III")) 
