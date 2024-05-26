class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #{(})
        prefix = []
        countopen = 0
        countclosed = 0
        if len(s) % 2 != 0:
            return False
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                countopen += 1
                prefix.append(s[i]) # kirjutame listi kõik avatud sulud
            else: # kui on suletud sulud siis kontrollime kas listis olevad sulud on samatüüpi kui suletud sulud
                if prefix == []: 
                    return False # kui jõuame siia siis järelikult on suletud sulg aga avatud sulgude list on tühi
                elif s[i] == ")" and prefix[-1] == "(":
                    countclosed += 1
                    prefix.pop()
                elif s[i] == "}" and prefix[-1] == "{":
                    countclosed += 1
                    prefix.pop()
                elif s[i] == "]" and prefix[-1] == "[":
                    countclosed += 1
                    prefix.pop()
                else:
                    return False
        if countopen != countclosed:
            return False
        return True