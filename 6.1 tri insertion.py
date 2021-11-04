
# tri par insertion
def tri_insertion(tab):
    # Accomplir de 1 à la taille qu'on a dans le tab
    for i in range(1, len(tab)):
        k = tab[i]
        j = i-1
        while j >= 0 and k < tab[j] :
                tab[j + 1] = tab[j]
                j -= 1
        tab[j + 1] = k
#on teste le programme qu'on a fait.
tab = [20,6,59,19,34] #le meme qu'on a fait dans le tri à bulle et selection
tri_insertion(tab)
print ("Le tableau trié est:")
for i in range(len(tab)):
    print ("% d" % tab[i])
