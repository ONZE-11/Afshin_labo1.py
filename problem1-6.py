sortie = False
while(not sortie):

    def menue():
        print("1- aficher votre nom ou votre Numero d`etudiant ")
        print("2- calcule nombre 1 puissan nombre2 ")
        print("3- le nombre est divisible par 2 ou 3 ?  ")
        print("4- a quel ane vous seriez 50 ans :  ")
        print("5- effectuer un operarion de 3 floats, le resultat avec 3 chiffres après la virgule  ")
        print("6- entrez votre repas , paye et l anne prefere :  ")
        print("7- sortir  ")
    menue()   
    no=int(input("choisir un nombre : " ))

    if no==1:
        
        def choisissez_nom_ou_nombre():
            
            print("#1. aficher votre nom: ")
            print("#2. aficher le Numero etudiant: ")

        option=int(input("aficher votre nom(1) ou aficher le Numero etudiant(2) : "))
        if option==1:
            print("Afshin Mahjoubi")

        elif option==2:
            print("2295368")

        else:
            print(" votre choix n est pas valid ! ")
       
        

    elif no==2:

        def faire_puissance (nombre1,nombre2):
            return(nombre1**nombre2)

        print("#1. entrez nombre1: ")
        print("#2. entrez nombre2: ")

        option1=int(input("Entrez nom(1): "))
        option2=int(input("Entrez nom(2): "))

        nombre1=option1
        nombre2=option2

        print(faire_puissance(nombre1,nombre2))

        

    elif no==3:


        def diviser_par_3_ou_3():
        
            Nombre=int(input("Entrez un nombre : "))


            if(Nombre%2==0):
                print("ce nombre est divisible par 2 :" ,Nombre )

            elif(Nombre%3==0):
                print("ce nombre est divisible par 3 :" ,Nombre )   

            else:
                print(Nombre)


        diviser_par_3_ou_3()
        


    elif no==4:

        from re import M


        def date_de_naissance(Nombre,m):
            return(Nombre+m)

        m=50    
        Nombre=int(input("Entrez votre année de naissance : "))


        print("vous etes 50 ans dans cette anne:" , date_de_naissance(Nombre,m))
        


    elif no==5:
        from unicodedata import decimal


        def multiplier_et_diviser( p1,p2,p3):
            return((p1*p2)/p3)

        p1=float(input("entrez premiere numero float :"))
        p2=float(input("entrez deuxieme numero float :"))
        p3=float(input("entrez troisieme numero float :"))

        mult=multiplier_et_diviser(p1,p2,p3)

        print(f"{mult:.3f}") 
        

    elif no==6:

        repas = str(input("entrez votre repas prefere : "))
        pays = str(input("entrez votre pays prefere : "))
        anne = str(input("entrez votre l'année future  : "))

        print(" Vous aurez l'opportunité de manger " , repas , "lorsque vous visiterai " , pays ,  "en" , anne ) 
        

    elif no==7:
        sortie=True

       


menue()