"""
Main script for franceinterbot.
"""

#Imports pour demandez_les_programmes()
from bs4 import BeautifulSoup
import requests

#Imports pour demandez_le_programme()
import os
import sys
from datetime import datetime, date, time
import json

#Imports
import tweepy
import configparser

#On se définit en France et en français, on définit le jour d'hui et l'heure
import locale

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
ajd = datetime.today()
he = ajd.hour
mi = ajd.minute

#On définit l'endroit où on travaille
franceinterbot_project_path = os.path.dirname(os.path.realpath(__file__))


def demandez_les_programmes():
    """
    Va chercher et lister les programmes du jour.
    Entrée :

    Sortie :
        -programmes_du_jour     list
    """
    #On va chercher le html de la page des programmes et on en fait une soupe
    url = 'https://www.franceinter.fr/programmes'
    liste_programmes = []

    page_programmes = requests.get(url)
    soupe = BeautifulSoup(page_programmes.text, "html.parser")

    #On morcelle le html dans une liste
    liste_article = []
    for article in soupe.find_all('article', "rich-section-list-gdp-item"):
        liste_article = liste_article + [str(article)]

    #A partir de la liste de html obtenue, on créé une liste de soupes
    liste_soupe = []
    for i in range(len(liste_article)):
        liste_soupe = liste_soupe + [BeautifulSoup(liste_article[i], "html.parser")]

    #On extrait des soupes les horaires, noms et urls des émissions diffusées et on les range dans des listes
    horaire_emission = []
    nom_emission = []
    url_info = []
    url_emission = []

    for i in range(len(liste_soupe)):

        horaire_emission = horaire_emission + [str(liste_soupe[i].find_all('div', class_='rich-section-list-gdp-item-start-date')).replace('\n','').replace('<div class="rich-section-list-gdp-item-start-date"><span>', '').replace('</span></div>]', '').replace('[','').replace(']','').strip()]

        nom_emission = nom_emission + [str(liste_soupe[i].find('a', class_='rich-section-list-gdp-item-content-show-emission-title').get('title'))]

        url_emission = url_emission + [str(liste_soupe[i].find('a', class_='rich-section-list-gdp-item-content-title').get('href'))]

    #On définit une liste de triplets [horaire, nom, url]
    programmes_du_jour = list(range(len(horaire_emission)))

    i = 0
    for i in range(len(horaire_emission)):
        programmes_du_jour[i] = [horaire_emission[i], nom_emission[i], url_emission[i]]

    #On retire de la liste les tuplets des émissions des nuits
    i = 0
    while i < len(programmes_du_jour):
        if programmes_du_jour[i][0][:3] == '00h' or programmes_du_jour[i][0][:3] == '01h' or programmes_du_jour[i][0][:3] == '02h' or programmes_du_jour[i][0][:3] == '03h' or programmes_du_jour[i][0][:3] == '04h':
            programmes_du_jour.remove(programmes_du_jour[i])
        else:
            i += 1

    return programmes_du_jour



def demandez_le_programme(programmes_du_jour):
    """
    Génère le message de publication.
    Entrée :

    Sortie :
        -le programme       str
    """
    triplet_programme = []
    h_programme = []
    mi_programme = []

    #On créer des listes heures et des minutes des horaires
    for i in range(len(programmes_du_jour)):

        if programmes_du_jour[i][0].split('h')[0][0] == '0':
            h_programme = h_programme + [programmes_du_jour[i][0].split('h')[0][1]]

        else:
            h_programme = h_programme + [programmes_du_jour[i][0].split('h')[0]]

        if programmes_du_jour[i][0].split('h')[1][0] == '0':
            mi_programme = mi_programme + [programmes_du_jour[i][0].split('h')[1][1]]

        else:
            mi_programme = mi_programme + [programmes_du_jour[i][0].split('h')[1]]

    #En fonction de l'horaire, on sélectionne le triplet correspondant au programme difusé
    for i in range(len(programmes_du_jour)):
        if h_programme[i] == str(he) and mi_programme[i] == str(mi):
            triplet_programme = programmes_du_jour[i]
            break

    #Si aucun triplet n'est selectionné, on ferme le programme
    if not(triplet_programme):
        sys.exit()

    les_nom_et_url = ''
    dico_nom_emissions = {}

    #On génère la publication selon le nom de l'émission diffusée, avec une execption pour le journal
    with open("listes_noms_emissions_inter.json", "r") as fichier:
        dico_nom_emissions = json.load(fichier)

        if triplet_programme[1] in dico_nom_emissions['liste1_heurede']:
            les_nom_et_url = ", l'heure de " + triplet_programme[1] + " sur France Inter.\n" + triplet_programme[2]

        elif triplet_programme[1] in dico_nom_emissions['liste2_heuredu']:
            les_nom_et_url = ", l'heure du " + triplet_programme[1] + " sur France Inter.\n" + triplet_programme[2]

        elif triplet_programme[1] in dico_nom_emissions['liste3_heuredubis']:
            les_nom_et_url = ", l'heure du " + triplet_programme[1][3:] + " sur France Inter.\n" + triplet_programme[2]

        elif triplet_programme[1] in dico_nom_emissions['liste4_heuredela']:
            les_nom_et_url = ", l'heure de la " + triplet_programme[1] + " sur France Inter.\n" + triplet_programme[2]

        elif triplet_programme[1] in dico_nom_emissions['liste5_heuredes']:
            les_nom_et_url = ", l'heure des " + triplet_programme[1] + " sur France Inter.\n" + triplet_programme[2]

        elif triplet_programme[1] in dico_nom_emissions['liste6_heuredesbis']:
            les_nom_et_url = ", l'heure des " + triplet_programme[1][4:] + " sur France Inter.\n" + triplet_programme[2]

        elif triplet_programme[1] in dico_nom_emissions['liste7_heured']:
            les_nom_et_url = ", l'heure d'" + triplet_programme[1] + " sur France Inter.\n" + triplet_programme[2]

        elif triplet_programme[1] in dico_nom_emissions['liste8_heuredel']:
            les_nom_et_url = ", l'heure de l'Hommage sur France Inter.\n" + triplet_programme[2]

        elif triplet_programme[1] in dico_nom_emissions['liste9_journaux']:
            les_nom_et_url = ", l'heure du journal sur France Inter.\n" + triplet_programme[2]

        elif triplet_programme[1] in dico_nom_emissions['liste10_journauxbis']:
            les_nom_et_url = ", l'heure du " + triplet_programme[1][13:] + " sur France Inter.\n" + triplet_programme[2]

        elif triplet_programme[1] in dico_nom_emissions['liste10_divers']:
            les_nom_et_url = ", " + triplet_programme[1] + " sur France Inter.\n" + triplet_programme[2]

        else:
            les_nom_et_url = ", l'heure de " + triplet_programme[1] + " sur France Inter.\n" + triplet_programme[2]

    #On définit l'horaire, en faisant en sorte que 'XXh00' devienne 'XXh'
    l_horaire = ''

    if triplet_programme[0].split('h')[1] == '0':
        l_horaire = triplet_programme[0].split('h')[0] + 'h'

    else:
        l_horaire = triplet_programme[0]

    #On définit le programme, avec un message spécial pour le matin et la minuit
    le_programme = ''

    if triplet_programme[1] == "Le 5/7" or triplet_programme[1] == "Le 6/9":
        le_programme = "Bonjour ! Il est " + l_horaire + les_nom_et_url

    elif he == 0 and mi == 0:
        le_programme = "Il est minuit, place aux rediffusions et à la musique sur France Inter."

    else:
        le_programme = "Il est " + l_horaire + les_nom_et_url


    return le_programme



if __name__ == "__main__":

    # read config file
    franceinterbot_project_path = os.path.dirname(os.path.realpath(__file__))
    config = configparser.ConfigParser()
    config.read(os.path.join(franceinterbot_project_path, "config", "config.ini"))
    consumer_key = config.get("access", "consumer_key")
    consumer_secret = config.get("access", "consumer_secret")
    access_token = config.get("access", "access_token")
    access_token_secret = config.get("access", "access_token_secret")

    # twitter authentification
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    programmes_du_jour = demandez_les_programmes()
    le_programme = demandez_le_programme(programmes_du_jour)

    api.update_status(status=le_programme)
