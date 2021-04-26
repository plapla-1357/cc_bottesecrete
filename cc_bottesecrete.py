from random import*

list_formulation = [ "va rendre heureux :","sera dans l'obligation de se demener pour donner un present a :",
    "va donner un cadeaux a :",
    "va jouer le père noël pour :",
    "deviendras, grace a son cadeau très bon ami avec :"]

def make_pairs_boucle(names):
    code = []
    br = "<br>"
    for i in range(len(names)-1):
        msg = f"{names[i]} {formulation_rd()} {names[i+1]}"
        code.append(msg)  
        code.append(br)
        print(msg)
    msg = f"{names[len(names)-1]} {formulation_rd()} {names[0]}"
    print(msg)
    code.append(msg)
    code.append(br)
    coden = " ".join(code)
    print(coden)
    return coden

def make_pairs(names):
    shuffle(names)
    return names

def formulation_rd():
    nb = randint(0,len(list_formulation)-1)
    return list_formulation[nb]
        



names = input("Entre les noms des participant(e)s, séparés par des virgules:")
names_new = names.split(",")



html = f'''
<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>Titre de la page</title>
  <link rel="stylesheet" href="style.css">
  <!--<script src="script.js"></script>-->
</head>
<body>
 {make_pairs_boucle(make_pairs(names_new))}
</body>
</html>
'''


fhtml = open("html.html","w")
fhtml.write(html)
fhtml.close()