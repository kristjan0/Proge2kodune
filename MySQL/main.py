import registreerimine
import sisselogimine

option = input("Kas soovid sisse logida (1) või registreerida (2)? ")
if option == "1":
    sisselogimine.sisselogimine()
elif option == "2":
    registreerimine.registreerimine()
else:
    print("Vali palun 1(sisselogimine) või 2(registreerimine)")
