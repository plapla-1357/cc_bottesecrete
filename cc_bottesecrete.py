from random import*

def make_pairs_boucle(names):
    for i in range(len(names)-1):
        print(f"{names[i]} va donner un cadeau a {names[i+1]}")
    print(f"{names[len(names)-1]} va donner un cadeau a {names[0]}")

def make_pairs(names):
    
    prs2_choisi = []
    #list_paire = {}
    for j in range(len(names)):
        finis = False
        while not finis:
            prs1 = randint(-1,len(names)-1)
            prs2 = randint(-1,len(names)-1)
            if prs1 != prs2 and prs2 not in prs_choisi:
                finis = True 
                prs2_choisi = prs_choisi.append(prs2)
                #list_paire[names[pers1]]=names[pers2]
                paire = [names[prs1],names[prs2]]
                print(f"{paire[0]} va donner un cadeau a {paire[1]}")
    


names = input("Entre les noms des participant(e)s, séparés par des virgules:")
names_new = names.split(",")

make_pairs(names_new)

