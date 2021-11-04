
def tri_bulle(tab):
    n = len(tab)
    # Passer tous les éléments du tableau sous le test
    for i in range(n):
        for j in range(0, n - i - 1):
            # échanger au cas où l'élément qui est trouvé est plus grand que l'élement suivant
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]


#on teste le programme qu'on a fait.
tab = [20,6,59,19,34]

tri_bulle(tab)

print("Le tableau trié est:")
for i in range(len(tab)):
    print("%d" % tab[i])


print("Le tableau trié est:")
for i in range(len(tab)):
    print("%d" % tab[i])
