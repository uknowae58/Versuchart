import os
from collections import defaultdict

# Chemin vers le dossier contenant les fichiers
dossier = 'S0_Messdaten'

'utiiliseer seulement si les fichiers nont pas ete renomme'
'''
# Parcours de tous les fichiers du dossier
for fichier in os.listdir(dossier):

    chemin_fichier = os.path.join(dossier, fichier)
    nouveau_nom = fichier[8:]  # Suppression de tout avant "IP23" y compris "IP23"
    nouveau_chemin = os.path.join(dossier, nouveau_nom)
    # Renommage du fichier
    os.rename(chemin_fichier, nouveau_chemin)'''

# Dictionnaire pour stocker les variations pour chaque position
variations = defaultdict(set)

# Parcours de tous les fichiers du dossier
for fichier in os.listdir(dossier):
    if fichier.endswith('.csv'):  # Vérification que le fichier est un fichier CSV
        chemin_fichier = os.path.join(dossier, fichier)

        # Extraction des groupes du nom de fichier
        groupes = fichier.split('.')[0].split('_')


        # Calcul des variations pour chaque position
        for position, groupe in enumerate(groupes, 1):
            # Ajout du symbole à la position courante dans l'ensemble des variations
            variations[position].add(groupe)

# Affichage du nombre de variations pour chaque position
for position, valeurs in variations.items():
    symbole_variations = len(valeurs)
    print(f"Position {position} : {symbole_variations}")
