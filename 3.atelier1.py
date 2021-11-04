def somme(n): #declarer la fonction de la somme
   if (n<=0) #si n est inferieur ou agal à 0
       return 0 #il va retourner 0
   else:
       return n + somme(n - 1)
n=int(input("entre votre nombre n =") )
print (somme(n))#afficher la somme
