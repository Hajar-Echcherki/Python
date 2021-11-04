
L1= [4,5,99,38,23,8,45,11,11,5] #pour definir une liste
dict={} #Pour initialiser un dictionnaire
for n in L1:
    L1.count(n) # Renvoie le nombre d'éléments ayant la valeur n dans la liste.
    dict[n]=L1.count(n) # pour associer une clé à une valeur
print (dict)
