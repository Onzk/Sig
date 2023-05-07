"""
Le module tools contient des petites
fonctions usuelles, nécessaires dans le 
programme.

"""

import json

import lxml.html.clean

import re

import config.config as config


# Définit l'emplacement du fichier
# contenant la <carte> des sites.
SITE_MAP_LOCATION = "scrapper/map.json"


def html_clean(text: str):
    """
    Cette fonction est chargée d'épurer une
    chaîne de caractères de tout contenu html.

    """
    return lxml.html.clean.Cleaner(

        style=True).clean_html(lxml.html.fromstring(

            re.sub(re.compile('<.*?>'), '', text))

    ).text_content().replace('\n', '').replace("'", "\\'").replace("  ", "")


def read_site_map():
    """
    Cette fonction est chargée de récupérer
    la <carte> des sites à scraper.

    """

    # On ouvre le fichier json contenant
    # la <carte> des sites à scraper.
    f = open(SITE_MAP_LOCATION, 'r')

    # On charge la <carte> sous forme de dictionnaire.
    map = json.loads(str(f.read()))

    # On ferme le fichier ouvert précédement.
    f.close()

    # On retourne la <carte>.
    return map


def get_site_map_urls():
    """
    Cette fonction est chargée de 
    renvoyer tous les sites paramètrés
    dans l'application.

    """
    return list(read_site_map())
