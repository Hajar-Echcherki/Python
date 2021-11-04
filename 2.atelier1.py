def conversion(nbr): ##la declaration du fonction conversion decimale to binaire
    if nbr > 1: #la condition
        conversion(nbr // 2)
    print(nbr % 2, end='')
#maintenant on va demander à l'utilisateur d'entrer un nombre
num = int(input("Entrez un nombre decimal: "))
conversion (num)