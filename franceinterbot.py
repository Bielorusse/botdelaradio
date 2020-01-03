"""
Main script for franceinterbot.
"""

import os
import sys
import datetime
import locale
import tweepy
import configparser

def demandez_le_programme():
    """
    Fourni heure par heure le programme de France Inter
    Sortie :
        -le_programme     str
    """

    from datetime import datetime, date, time

    locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

    ajd = datetime.today()
    y = ajd.year
    mo = ajd.month
    d = ajd.day
    h = ajd.hour
    mi = ajd.minute


    """
    Programmes des lundi, mardi, mercredi et jeudi
    """

    if ajd.isoweekday() == 1 or ajd.isoweekday() == 2 or ajd.isoweekday() == 3 or ajd.isoweekday() == 4:

        if h == 5 and mi == 0:
            le_programme = "Bonjour ! Il est 5h, l'heure du 5/7 sur France Inter.\n https://www.franceinter.fr/emissions/le-5-7/le-5-7-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 7 and mi == 0:
            le_programme = "Il est 7h, l'heure du 7/9 sur France Inter.\n https://www.franceinter.fr/emissions/le-7-9/le-7-9-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 9 and mi == 0:
            le_programme = "Il est 9h, l'heure de Boomerang sur France Inter.\n https://www.franceinter.fr/emissions/boomerang/boomerang-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 9 and mi == 40:
            le_programme = "Il est 9h40, l'heure de L'instant M sur France Inter.\n https://www.franceinter.fr/emissions/l-instant-m/l-instant-m-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 10 and mi == 0:
            le_programme = "Il est 10h, l'heure de Grand bien vous fasse sur France Inter.\n https://www.franceinter.fr/emissions/grand-bien-vous-fasse/grand-bien-vous-fasse-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 11 and mi == 0:
            le_programme = "Il est 11h, l'heure de La bande originale sur France Inter.\n https://www.franceinter.fr/emissions/la-bande-originale/la-bande-originale-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 12 and mi == 30:
            le_programme = "Il est 12h30, l'heure des Carnets de campagne sur France Inter.\n https://www.franceinter.fr/emissions/carnets-de-campagne/carnets-de-campagne-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 12 and mi == 45:
            le_programme = "Il est 12h45, l'heure du jeu des 1000 € sur France Inter.\n https://www.franceinter.fr/emissions/le-jeu-des-1000-eu/le-jeu-des-1000-eu-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 13 and mi == 0:
            le_programme = "Il est 13h, l'heure du journal de 13h sur France Inter.\n https://www.franceinter.fr/emissions/le-journal-de-13h/le-journal-de-13h-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 13 and mi == 30:
            le_programme = "Il est 13h30, l'heure de La terre au carré sur France Inter.\n https://www.franceinter.fr/emissions/la-terre-au-carre/la-terre-au-carre-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 14 and mi == 30:
            le_programme = "Il est 14h30, l'heure de La marche de l'histoire sur France Inter.\n https://www.franceinter.fr/emissions/la-marche-de-l-histoire/la-marche-de-l-histoire-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 15 and mi == 0:
            le_programme = "Il est 15h, l'heure des Affaires sensibles sur France Inter.\n https://www.franceinter.fr/emissions/affaires-sensibles/affaires-sensibles-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 16 and mi == 0:
            le_programme = "Il est 16h, l'heure de Popopop sur France Inter.\n https://www.franceinter.fr/emissions/popopop/popopop-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 17 and mi == 0:
            le_programme = "Il est 17h, l'heure de Par Jupiter ! sur France Inter.\n https://www.franceinter.fr/emissions/par-jupiter/par-jupiter-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 18 and mi == 0:
            le_programme = "Il est 18h, l'heure du journal de 18h sur France Inter.\n https://www.franceinter.fr/emissions/le-journal-de-18h/le-journal-de-18h-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 18 and mi == 15:
            le_programme = "Il est 18h15, l'heure d'Un jour dans le monde sur France Inter.\n https://www.franceinter.fr/emissions/un-jour-dans-le-monde/un-jour-dans-le-monde-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 19 and mi == 0:
            le_programme = "Il est 19h, l'heure du journal de 19h sur France Inter.\n https://www.franceinter.fr/emissions/le-journal-de-19h/le-journal-de-19h-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 19 and mi == 20:
            le_programme = "Il est 19h20, l'heure du téléphone sonne sur France Inter.\n https://www.franceinter.fr/emissions/le-telephone-sonne/le-telephone-sonne-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 20 and mi == 0:
            le_programme = "Il est 20h, l'heure bleue sur France Inter.\n https://www.franceinter.fr/emissions/l-heure-bleue/l-heure-bleue-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 21 and mi == 0:
            le_programme = "Il est 21h, l'heure de Very good trip sur France Inter.\n https://www.franceinter.fr/emissions/very-good-trip/very-good-trip-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 22 and mi == 0:
            le_programme = "Il est 22h, l'heure du nouveau rendez-vous sur France Inter.\n https://www.franceinter.fr/emissions/le-nouveau-rendez-vous/le-nouveau-rendez-vous-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 23 and mi == 0:
            le_programme = "Il est 23h, l'heure du journal de 23h sur France Inter.\n https://www.franceinter.fr/emissions/le-journal-de-23h/le-journal-de-23h-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 23 and mi == 15:
            le_programme = "Il est 23h15, l'heure du nouveau rendez-vous : France Inter + sur France Inter.\n https://www.franceinter.fr/emissions/le-nouveau-rendez-vous-france-inter/le-nouveau-rendez-vous-france-inter-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 23 and mi == 59: # on lance le programme de nuit, on peut tricher un peu ;)
            le_programme = "C'est la nuit. Place aux rediffusions et à la musique sur France Inter."

        else:
            sys.exit()


    """
    Programme du vendredi
    """

    if ajd.isoweekday() == 5:

        if h == 5 and mi == 0:
            le_programme = "Bonjour ! Il est 5h, l'heure du 5/7 sur France Inter.\n https://www.franceinter.fr/emissions/le-5-7/le-5-7-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 7 and mi == 0:
            le_programme = "Il est 7h, l'heure du 7/9 sur France Inter.\n https://www.franceinter.fr/emissions/le-7-9/le-7-9-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 9 and mi == 0:
            le_programme = "Il est 9h, l'heure de Boomerang sur France Inter.\n https://www.franceinter.fr/emissions/boomerang/boomerang-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 9 and mi == 40:
            le_programme = "Il est 9h40, l'heure de L'instant M sur France Inter.\n https://www.franceinter.fr/emissions/l-instant-m/l-instant-m-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 10 and mi == 0:
            le_programme = "Il est 10h, l'heure de Grand bien vous fasse sur France Inter.\n https://www.franceinter.fr/emissions/grand-bien-vous-fasse/grand-bien-vous-fasse-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 11 and mi == 0:
            le_programme = "Il est 11h, l'heure de La bande originale sur France Inter.\n https://www.franceinter.fr/emissions/la-bande-originale/la-bande-originale-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 12 and mi == 30:
            le_programme = "Il est 12h30, l'heure des Carnets de campagne sur France Inter.\n https://www.franceinter.fr/emissions/carnets-de-campagne/carnets-de-campagne-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 12 and mi == 45:
            le_programme = "Il est 12h45, l'heure du jeu des 1000 € sur France Inter.\n https://www.franceinter.fr/emissions/le-jeu-des-1000-eu/le-jeu-des-1000-eu-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 13 and mi == 0:
            le_programme = "Il est 13h, l'heure du journal de 13h sur France Inter.\n https://www.franceinter.fr/emissions/le-journal-de-13h/le-journal-de-13h-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 13 and mi == 30:
            le_programme = "Il est 13h30, l'heure de La terre au carré sur France Inter.\n https://www.franceinter.fr/emissions/la-terre-au-carre/la-terre-au-carre-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 14 and mi == 30:
            le_programme = "Il est 14h30, l'heure de La marche de l'histoire sur France Inter.\n https://www.franceinter.fr/emissions/la-marche-de-l-histoire/la-marche-de-l-histoire-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 15 and mi == 0:
            le_programme = "Il est 15h, l'heure des Affaires sensibles sur France Inter.\n https://www.franceinter.fr/emissions/affaires-sensibles/affaires-sensibles-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 16 and mi == 0:
            le_programme = "Il est 16h, l'heure de Popopop sur France Inter.\n https://www.franceinter.fr/emissions/popopop/popopop-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 17 and mi == 0:
            le_programme = "Il est 17h, l'heure de Par Jupiter ! sur France Inter.\n https://www.franceinter.fr/emissions/par-jupiter/par-jupiter-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 18 and mi == 0:
            le_programme = "Il est 18h, l'heure du journal de 18h sur France Inter.\n https://www.franceinter.fr/emissions/le-journal-de-18h/le-journal-de-18h-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 18 and mi == 15:
            le_programme = "Il est 18h15, l'heure d'Une semaine en France sur France Inter.\n https://www.franceinter.fr/emissions/une-semaine-en-france/une-semaine-en-france-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 19 and mi == 0:
            le_programme = "Il est 19h, l'heure du journal de 19h sur France Inter.\n https://www.franceinter.fr/emissions/le-journal-de-19h/le-journal-de-19h-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 19 and mi == 20:
            le_programme = "Il est 19h20, l'heure du téléphone sonne sur France Inter.\n https://www.franceinter.fr/emissions/le-telephone-sonne/le-telephone-sonne-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 20 and mi == 0:
            le_programme = "Il est 20h, l'heure de Pas son genre sur France Inter.\n https://www.franceinter.fr/emissions/pas-son-genre/pas-son-genre-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 21 and mi == 0:
            le_programme = "Il est 21h, l'heure de Côté club sur France Inter.\n https://www.franceinter.fr/emissions/cote-club/cote-club-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 23 and mi == 0:
            le_programme = "Il est 23h, l'heure du journal de 23h sur France Inter.\n https://www.franceinter.fr/emissions/le-journal-de-23h/le-journal-de-23h-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 23 and mi == 15:
            le_programme = "Il est 23h15, l'heure du journal de 23h sur France Inter.\n https://www.franceinter.fr/emissions/le-nouveau-rendez-vous-france-inter/le-nouveau-rendez-vous-france-inter-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 23 and mi == 59:
            le_programme = "C'est la nuit. Place aux rediffusions et à la musique sur France Inter."

        else:
            sys.exit()


    """
    Programme du samedi
    """

    if ajd.isoweekday() == 6:

        if h == 6 and mi == 0:
            le_programme = "Bonjour ! Il est 6h, l'heure du 6/9 du week-end sur France Inter.\n https://www.franceinter.fr/emissions/le-6-9/le-6-9-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 9 and mi == 0:
            le_programme = "Il est 9h, l'heure d'On n'arrête pas l'éco sur France Inter.\n https://www.franceinter.fr/emissions/on-n-arrete-pas-l-eco/on-n-arrete-pas-l-eco-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 10 and mi == 0:
            le_programme = "Il est 10h, l'heure d'On aura tout vu sur France Inter.\n https://www.franceinter.fr/emissions/on-aura-tout-vu/on-aura-tout-vu-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 11 and mi == 0:
            le_programme = "Il est 11h, l'heure de Sur les épaules de Darwin sur France Inter.\n https://www.franceinter.fr/emissions/sur-les-epaules-de-darwin/sur-les-epaules-de-darwin-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 12 and mi == 0:
            le_programme = "Il est midi, l'heure du grand face à face sur France Inter.\n https://www.franceinter.fr/emissions/le-grand-face-a-face/le-grand-face-a-face-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 13 and mi == 0:
            le_programme = "Il est 13h, l'heure du journal de 13h du week-end sur France Inter.\n https://www.franceinter.fr/emissions/le-journal-de-13h-du-week-end/le-journal-de-13h-du-week-end-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 13 and mi == 20:
            le_programme = "Il est 13h20, l'heure des Secrets d'info sur France Inter.\n https://www.franceinter.fr/emissions/secrets-d-info/secrets-d-info-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 14 and mi == 0:
            le_programme = "Il est 14h, l'heure de La librairie francophone sur France Inter.\n https://www.franceinter.fr/emissions/la-librairie-francophone/la-librairie-francophone-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 15 and mi == 0:
            le_programme = "Il est 15h, l'heure de Du vent dans les synapses sur France Inter.\n https://www.franceinter.fr/emissions/du-vent-dans-les-synapses/du-vent-dans-les-synapses-{0:%d}-{0:%B}-{0:%Y}-0".format(ajd)

        elif h == 16 and mi == 0:
            le_programme = "Il est 16h, l'heure la seconde partie de Du vent dans les synapses sur France Inter.\n https://www.franceinter.fr/emissions/du-vent-dans-les-synapses/du-vent-dans-les-synapses-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 17 and mi == 0:
            le_programme = "Il est 17h, l'heure de La preuve par Z sur France Inter.\n https://www.franceinter.fr/emissions/la-preuve-par-z/la-preuve-par-z-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 18 and mi == 0:
            le_programme = "Il est 18h, l'heure du journal de 18h du week-end sur France Inter.\n https://www.franceinter.fr/emissions/le-journal-de-18h-du-week-end/le-journal-de-18h-du-week-end-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 18 and mi == 10:
            le_programme = "Il est 18h10, l'heure de Ça peut pas faire de mal sur France Inter.\n https://www.franceinter.fr/emissions/ca-peut-pas-faire-de-mal/ca-peut-pas-faire-de-mal-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 19 and mi == 0:
            le_programme = "Il est 19h, l'heure du journal de 19h du week-end sur France Inter.\n https://www.franceinter.fr/emissions/le-journal-de-19h-du-week-end/le-journal-de-19h-du-week-end-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 19 and mi == 20:
            le_programme = "Il est 19h20, l'heure de L'humeur vagabonde sur France Inter.\n https://www.franceinter.fr/emissions/l-humeur-vagabonde/l-humeur-vagabonde-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 19 and mi == 55:
            le_programme = "Il est 19h55, l'heure d'Expression directe sur France Inter.\n https://www.franceinter.fr/emissions/expression-directe/expression-directe-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 20 and mi == 0:
            le_programme = "Il est 20h, Une heure en séries sur France Inter.\n https://www.franceinter.fr/emissions/une-heure-en-series/une-heure-en-series-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 21 and mi == 0:
            le_programme = "Il est 21h, l'heure du grand urbain sur France Inter.\n https://www.franceinter.fr/emissions/le-grand-urbain/le-grand-urbain-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 22 and mi == 00:
            le_programme = "Il est 22h00, l'heure de Foule continentale sur France Inter.\n https://www.franceinter.fr/emissions/foule-continentale/foule-continentale-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 23 and mi == 0:
            le_programme = "Il est 23h, l'heure du journal de 23h du week-end sur France Inter.\n https://www.franceinter.fr/emissions/le-journal-de-23h-du-week-end/le-journal-de-23h-du-week-end-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 23 and mi == 15:
            le_programme = "Il est 23h15, l'heure de C'est bientôt demain sur France Inter.\n https://www.franceinter.fr/emissions/c-est-bientot-demain/c-est-bientot-demain-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 23 and mi == 35:
            le_programme = "Il est 23h35, l'heure des vies françaises sur France Inter.\n https://www.franceinter.fr/emissions/des-vies-francaises/des-vies-francaises-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 23 and mi == 59:
            le_programme = "C'est la nuit. Place aux rediffusions et à la musique sur France Inter."

        else:
            sys.exit()


    """
    Programme du dimanche
    """

    if ajd.isoweekday() == 7:

        if h == 6 and mi == 0:
            le_programme = "Bonjour ! Il est 6h, l'heure du 6/9 du week-end sur France Inter.\n https://www.franceinter.fr/emissions/le-6-9/le-6-9-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 9 and mi == 0:
            le_programme = "Il est 9h, l'heure d'Interception sur France Inter.\n https://www.franceinter.fr/emissions/interception/interception-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 10 and mi == 0:
            le_programme = "Il est 10h, l'heure de Remède à la mélancolie sur France Inter.\n https://www.franceinter.fr/emissions/remede-a-la-melancolie/remede-a-la-melancolie-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 11 and mi == 0:
            le_programme = "Il est 11h, l'heure d'On va déguster sur France Inter.\n https://www.franceinter.fr/emissions/on-va-deguster/on-va-deguster-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 12 and mi == 0:
            le_programme = "Il est midi, l'heure des Questions politiques sur France Inter.\n https://www.franceinter.fr/emissions/questions-politiques/questions-politiques-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 13 and mi == 0:
            le_programme = "Il est 13h, l'heure du journal de 13h du week-end sur France Inter.\n https://www.franceinter.fr/emissions/le-journal-de-13h-du-week-end/le-journal-de-13h-du-week-end-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 13 and mi == 20:
            le_programme = "Il est 13h20, l'heure de CO2 mon amour sur France Inter.\n https://www.franceinter.fr/emissions/co2-mon-amour/co2-mon-amour-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 14 and mi == 0:
            le_programme = "Il est 14h, l'heure d'Une journée particulière sur France Inter.\n https://www.franceinter.fr/emissions/une-journee-particuliere/une-journee-particuliere-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 15 and mi == 0:
            le_programme = "Il est 15h, l'heure du grand atelier sur France Inter.\n https://www.franceinter.fr/emissions/le-grand-atelier/le-grand-atelier-{0:%d}-{0:%B}-{0:%Y}-0".format(ajd)

        elif h == 17 and mi == 0:
            le_programme = "Il est 17h, l'heure d'Et je remets le son sur France Inter.\n https://www.franceinter.fr/emissions/et-je-remets-le-son/et-je-remets-le-son-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 18 and mi == 0:
            le_programme = "Il est 18h, l'heure du journal de 18h du week-end sur France Inter.\n https://www.franceinter.fr/emissions/le-journal-de-18h-du-week-end/le-journal-de-18h-du-week-end-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 18 and mi == 10:
            le_programme = "Il est 18h10, l'heure de L'œil du tigre sur France Inter.\n https://www.franceinter.fr/emissions/l-oeil-du-tigre/l-oeil-du-tigre-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 19 and mi == 0:
            le_programme = "Il est 19h, l'heure du journal de 19h du week-end sur France Inter.\n https://www.franceinter.fr/emissions/le-journal-de-19h-du-week-end/le-journal-de-19h-du-week-end-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 19 and mi == 30:
            le_programme = "Il est 19h30, l'heure des p'tits bateaux sur France Inter.\n https://www.franceinter.fr/emissions/les-p-tits-bateaux/les-p-tits-bateaux-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 19 and mi == 55:
            le_programme = "Il est 19h55, l'heure de L'as-tu lu mon p'tit loup sur France Inter.\n https://www.franceinter.fr/emissions/l-as-tu-lu-mon-p-tit-loup/l-as-tu-lu-mon-p-tit-loup-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 20 and mi == 0:
            le_programme = "Il est 20h, l'heure du masque et la plume sur France Inter.\n https://www.franceinter.fr/emissions/le-masque-et-la-plume/le-masque-et-la-plume-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 21 and mi == 0:
            le_programme = "Il est 21h, l'heure d'Autant en emporte l'histoire sur France Inter.\n https://www.franceinter.fr/emissions/autant-en-emporte-l-histoire/autant-en-emporte-l-histoire-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 22 and mi == 00:
            le_programme = "Il est 22h00, l'heure de Modern Love sur France Inter.\n https://www.franceinter.fr/emissions/modern-love/modern-love-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 23 and mi == 0:
            le_programme = "Il est 23h, l'heure du journal de 23h du week-end sur France Inter.\n https://www.franceinter.fr/emissions/le-journal-de-23h-du-week-end/le-journal-de-23h-du-week-end-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 23 and mi == 15:
            le_programme = "Il est 23h15, l'heure de la suite de Mordern Love sur France Inter.\n https://www.franceinter.fr/emissions/modern-love/modern-love-{0:%d}-{0:%B}-{0:%Y}".format(ajd)

        elif h == 23 and mi == 59:
            le_programme = "C'est la nuit. Place aux rediffusions et à la musique sur France Inter."

        else:
            sys.exit()

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

    le_programme = demandez_le_programme()

    api.update_status(status=le_programme)
