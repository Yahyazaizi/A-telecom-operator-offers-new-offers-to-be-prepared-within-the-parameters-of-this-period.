def offre(duree):
    if(duree >120 ):
        off1 = (duree - 120)*0.5
        off2 = (duree - 60)
        off3 = (duree - 30) * 1.5
        off4 =  duree* 2
    elif(duree <= 120 and duree >60):
        off1 =0
        off2 =  (duree - 60)
        off3 = (duree - 30) * 1.5
        off4 = duree * 2
    elif (duree <= 60 and duree > 30):
        off1 = 0
        off2 = 0
        off3 = (duree - 30) * 1.5
        off4 = duree * 2
    elif (duree <= 30 ):
        off1 = 0
        off2 = 0
        off3 = 0
        off4 = duree * 2
    list = [off1, off2, off3, off4]
    return list
d=0
while True:
    print("Menu :")
    print("1. Option 1.la durre de communication en min ")
    print("2. Option 2.la liste du cout mensuelle par offre")
    print("3. Option 3.l offre le plus interesasante")
    print("4. Quitter")
    choix = input("Sélectionnez une option : ")
    if choix == '1':
        d = int(input("donner la durre de communication en min  en mois: "))
    elif choix == '2':
        offre(d)
        print("le cout mensuelle pour l offre de 200 dh est : 0dh")
        print("le cout mensuelle pour l offre de 100 dh est :","le prix par moi",offre(d)[0],"dh")
        print("le cout mensuelle pour l offre de 50 dh est :","le prix par moi", offre(d)[1],"dh")
        print("le cout mensuelle pour l offre de 20 dh est :","le prix par moi", offre(d)[2],"dh")
        print("le cout mensuelle pour l offre de 0 dh est :","le prix par moi",  offre(d)[3],"dh")
    elif choix == '3':
        m=min(offre(d))
        indice = offre(d).index(m)

        print("l offre le plus interesasante est le :",indice+1)
    elif choix == '4':
        print("Quitter le programme.")
        break
    else:
        print("Option invalide. Veuillez sélectionner une option valide (1, 2, 3, 4, ou 5).")