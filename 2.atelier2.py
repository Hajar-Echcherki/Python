
L = [4 ,9 ,27 ,78,7,30,2,5,6] #definir une liste
a=len(L)//3 # len renvoie le nombre des éléments dans une liste , ici on la devise sur 3.
b=2*len(L)//3
L1=L[:a]
L2=L[a:b]
L3=L[b:]
print (L1[::-1],L2[::-1],L3[::-1]) #pour inverser chaque morceau
