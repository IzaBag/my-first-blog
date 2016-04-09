ilosc_osob=int(input("Z iloma osobami mam przyjemnosc rozmawiac?"))

osoby = []
for i in range(ilosc_osob):
    dane=input("Podaj imie osoby")
    osoby.append(dane)
print (osoby)

wiekosob = {}
for i in range(ilosc_osob):
    dane1=input("Ile " + osoby[i] + " ma lat?")
    wiekosob[osoby[i]]=dane1
print (wiekosob)


#
# imie=input("Jak masz na imie?")
#
# def hej(imie):
#     if imie=="Iza":
#         print ("siema Iza!")
#     elif imie=="Ola":
#         print ("hejka Ola!")
#     else:
#         print ("witaj " + imie + "!")
#
# hej(imie)
#
# dziewczyny = ["Iza", "Ola", "Asia"]
# print ("Widze, ze jest was wiecej!")
# for imie in dziewczyny:
#     hej(imie)
#

# wiek1=int(input("Ile masz lat?"))
#
# def age(wiek):
#     if wiek<=25:
#         print ("Ale z ciebie mlodzieniaszek!")
#     elif wiek>25 and wiek<30:
#         print ("Oj, jestes na skraju mlodosci")
#     else:
#         print ("Ale duzo!")
#
# age(wiek)
#
# liczby=input("Wpiszcie swoj wiek po przecinku bez spacji")
# lata=liczby.split(",")
# print (lata)
#
# for i in range(len(lata)):
#     lata[i]=int(lata[i])
#
# print (lata)
#
# lata_dziewczyn = {}
#
# for i,imie in enumerate(dziewczyny):
#     lata_dziewczyn[imie]=lata[i]
#
# print (lata_dziewczyn)
