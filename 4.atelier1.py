def fibonacci(a)#declarer la fonction de fibonacci
    if(a <= 1): #si a est inferieur ou egale à 1
        return a #on va retourner a
    else:
        return (fibonacci(a-1) + fibonacci(a-2))
a = int(input("Entrez le nombre de termes que vous voulez:"))
print("Suite de Fibonacci en utilisant la recursion :")
for i in range(a):
    print(fibonacci(i))#resultat