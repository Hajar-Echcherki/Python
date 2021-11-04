set_1={6,3,56,73,45,78} #definir le premier set
set_2={6,8,23,3,45,68} #definir le dexieme set
set_3={}
set_3 =set_1&set_2
print (set_3) #afficher le 3 eme set
for i in set_3:
    set_1.remove(i) #pour supprimer la valeur requise donnée  de la liste
    set_2.remove(i)
print (set_1)  #afficher la liste apres la supression d'element
print(set_2)
