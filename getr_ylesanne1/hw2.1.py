  def addDigits(self, num: int) -> int:
        if num<10: #kui arv on vaiksem, kui 10 returnib selle
            return num

        if num%9==0:
            return 9
        else:
            return num%9 #kui miski muu siis returnib numbri jaagi