def compte (n) : #declaration du fonction
   num=0
   while n!=0 :
       n=int(n/10) #la division sur 10
       num=num+1
   return num #il va retourner num
n=int (input("ecrire un nombre :"))
print ("le nombre totale est ",n,"est",compte(n)) #affiche du compte(n)
