"""
Le module crawler.crawler permet de lancer le scrapping 
via ligne de commande, de façon transparente.

"""

import subprocess
import threading
import tools


def crawl() -> dict:
    """
    Cette fonction est chargée de lancer le scraping.

    """
    
    # On récupère la liste des sites paramètrés.
    urls = tools.get_site_map_urls()

    # On parcours cette liste.
    for url in urls:

        # On affiche l'url.
        print(f'#Scraping : {url}')

        # On lance la commande pour scraper l'url.
        threading.Thread(target=lambda url: subprocess.run(

            f'python -m scrapy crawl news -a url="{url}"', capture_output=True), args=(url,)

        ).start()

    # On renvoie une réponse sur le processus et les sites scrapés.
    return {"scrapping": "In process...", "urls": tools.get_site_map_urls()}
