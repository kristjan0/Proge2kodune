import rsa
 
publicKey, privateKey = rsa.newkeys(512)
 
message = input("kirjuta textt: ") #küsib kasutajalt teksti mida cryptida
encMessage = rsa.encrypt(message.encode(), publicKey) #krüpteerib sisestatud teksti
print("krüpteeritud tekst: ", encMessage) 
 
decMessage = rsa.decrypt(encMessage, privateKey).decode() #dekrüpteerib teksti
print("dekrüpteeritud tekst: ", decMessage)

f = open("avalik_võti.txt", "w") #teeb faili avalik_võti.txt kuhu lisab public key
f.write(str(publicKey))

fdec = open("privaatne_võti", "w") #teeb faili privaatne_võti.txt kuhu lisab private key
fdec.write(str(privateKey))