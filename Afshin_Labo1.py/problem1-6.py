def choisissez_nom_ou_nombre():
    print("#1. Afshin: ")
    print("#2. Nombre: ")

option=int(input("Entrez nom(1) ou nombre(2) : "))
if option==1:
    print("Afshin")

elif(option==2):
    print("2295368")

else:
    print(" votre choix n est pas valid ! ")
    
    
    
    
#problem2

def faire_puissance (nombre1,nombre2):
    return(nombre1**nombre2)

print("#1. entrez nombre1: ")
print("#2. entrez nombre2: ")

option1=int(input("Entrez nom(1): "))
option2=int(input("Entrez nom(2): "))

nombre1=option1
nombre2=option2

print(faire_puissance(nombre1,nombre2))




#problem3

def diviser_par_3_ou_3():
  
    Nombre=int(input("Entrez un nombre : "))


    if(Nombre%2==0):
        print("ce nombre est divisible par 2 :" ,Nombre )

    if(Nombre%3==0):
        print("ce nombre est divisible par 3 :" ,Nombre )   

    
diviser_par_3_ou_3()




#problem 4

from re import M


def date_de_naissance(Nombre,m):
    return(Nombre+m)

m=50    
Nombre=int(input("Entrez votre année de naissance : "))


print("vous etes 50 ans dans cette anne:" , date_de_naissance(Nombre,m))





#problem5

from unicodedata import decimal


def multiplier_et_diviser( p1,p2,p3):
    return((p1*p2)/p3)

p1=round(7.250)
p2=round(10.725)
p3=round(2.256)

print(multiplier_et_diviser(p1,p2,p3)) 





#problem6

repas = str(input("entrez votre repas prefere : "))
pays = str(input("entrez votre pays prefere : "))
anne = str(input("entrez votre l'année future  : "))

print(" Vous aurez l'opportunité de manger " , repas , "lorsque vous visiterai " , pays ,  "en" , anne ) 


