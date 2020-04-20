taille=float(input("Quel est votre taille en mètre ? "))
poids=float(input("Quel est votre poids en kilos ? "))
print("Vous mesurez ", taille," m, et pesez ", poids)
IMC=(poids/(taille*taille))
print("Votre IMC est ", "% 12.2f" %IMC)
if IMC<18.5 :
    print("Vous êtes en état de maigreur.")
elif IMC<24.9 :
    print("Vous êtes normal.")
elif IMC<40 :
    print("Vous êtes obèse.")
else:
    print("Vous êtes en état d'obésité massive.")
