
L1 = [13 ,2,4,6]#saisir la premier liste
L2= [9,14,54,13]#dexieme liste
L3=[]#troisieme liste
n=0
for i in L3:
    if n%2 !=0 : #trouver des index impairs
      L3.append(i)#ajouter un element à la liste
    n += 1
for j in L2:
    if n %2 ==0 :#trouver des indes paires
      L3.append(j)
    n +=1
print(L3)
