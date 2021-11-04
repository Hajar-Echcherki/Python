def factoriel (i): #la declaration du fonction qui va calculer le factoriel
  if i==1 : #boucle de condition
    return 1 #il va retourner 1
  else :
    return i*factoriel(i-1)
n=int (input ("entrer le nombre n=")) # renvoie une valeur dont le type correspond à ce que l'utilisateur a entré.
som=0
for i in range (1,n+1,1):
    som = som+factoriel(i)/i
print(som)#afficher la somme
