
def tri_selection(tab):
    for i in range(len(tab)):
        #pour trouber le min
        min = i
        for j in range(i + 1, len(tab)):
            if tab[min] > tab[j]:
                min = j

        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp
    return tab


#on teste le programme qu'on a fait.
tab = [20,6,59,19,34]
tri_selection(tab)

print("Le tableau trié est:")
for i in range(len(tab)):
    print("%d" % tab[i])
