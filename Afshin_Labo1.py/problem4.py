from re import M


def date_de_naissance(Nombre,m):
    return(Nombre+m)

m=50    
Nombre=int(input("Entrez votre année de naissance : "))


print("vous etes 50 ans dans cette anne:" , date_de_naissance(Nombre,m))
