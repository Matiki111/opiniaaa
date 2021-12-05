import random
import time

opinia = input("wykaz swoja opinie: ")


racja = ['true','same','rel','nie masz racji bracie!','ojjjj grubo sie mylisz','chyba twoja stara','punkt', 'racje masz'
         'kornik']
racjeMasz = random.choice(racja)

print("Oto co sądze o twojej opini: " + str(racjeMasz))
time.sleep(1)

same = int(input("Napisz od 1 do 10 jak bardzo zgadzasz sie z moją responsą: "))
if same == 0:
    print("Smutno mi..., aczkolwiek wiem, że to tylko moja opinia i każdy ma prawo się z nią nie zgadzać!")
elif same == 1 or same == 2:
    print("Widzę jakiś płomyczek nadziei skoro nie dałeś 0, aczkolwiek wciąż serce boli...")
elif same == 3 or same == 4 or same == 5:
    print("Widzę iż muszę poćwiczyć opiniotwórstwo, dzięki za responsę")
elif same == 6 or same == 7:
    print("Yay! powyżej połowy to dla mnie zaszczyt!")
elif same == 8 or same == 9:
    print("Literalnie aktualnie fortunnie jestem bogiem opiniotwórstwa")
elif same == 10:
    print("MOJA OPINIA = TWOJA OPINIA COS NIESAMOWITEGO ZE MAMY TAKIE SAME POGLADY UWU")
else:
    print("prosze mnie tu nie scamowac!")

time.sleep(1)
print("wesołej kawusi")
input()