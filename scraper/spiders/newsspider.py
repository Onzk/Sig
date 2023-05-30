"""
Le module scraper.spiders.newsspider contient 
le scrapeur qui permet de récupérer les articles
en ligne, et de les stockés dans la base de données.
Il utilise le fichier 'map.json', pour déterminer
les emplacements des valeurs à prendre.

"""


import scrapy

from database.models.article import Article

import database.db as db

import tools


class NewsSpider(scrapy.Spider):
    """
    Cette classe représente le scrapeur
    qui permet de récupérer les données en ligne
    et de les stocker dans la base de données. 

    """

    # Définit le nom du spider,
    # pour une le lancement en ligne de
    # commande.
    name = "news"

    # custom_settings = { 'CLOSESPIDER_ITEMCOUNT': 150 }

    # Définit le site courrant en cours de scraping
    site = {}

    def __init__(self, name=None, **kwargs):
        """
        Cette fonction est le constructeur de la classe.

        """

        # On appèle le constructeur de la classe mère.
        super().__init__(name, **kwargs)

        # Définit les urls à scraper,
        # récupérés directement depuis les
        # paramètres passés en ligne de commande.
        self.start_urls = [kwargs.get('url')]

    async def parse(self, response):
        """
        Cette fonction est chargée de scraper le 
        contenu d'une page web, depuis son url.

        """

        # On ignore les erreurs au niveau du site
        # pour éviter les latences.
        try:

            # On vérifie que la page n'a pas été
            # signalée comme ayant un système de
            # pagination.
            if not ("next_page" in self.site):

                # On charge la <carte> de l'url courant.
                self.site = tools.read_site_map()[response.url]

            # On parcours les articles retrouvés en ligne.
            for article in response.css(self.site['articles']):

                # Définit l'url pour consulter cet article.
                article_url = article.css(self.site['article_link']).get()

                # On lance une requête de scraping sur l'url en absolu de l'article.
                yield scrapy.Request(response.urljoin(article_url), callback=self.parse_articles)

            # On vérifie si la page courrante a un système
            # de pagination d'après sa carte.
            if "next_page" in self.site:

                # On récupère l'url de la page suivante.
                next_page = response.css(

                    self.site['next_page']).extract_first()

                # On vérifie s'il existe une page qui suit.
                if next_page:

                    # On lance une requête pour parser la page qui suit.
                    yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

        except Exception:

            # S'il y a une exception au niveau du site,
            # on l'ignore.
            pass

    async def parse_articles(self, response):
        """
        Cette fonction est chargée de scraper le 
        contenu d'un article, depuis son url.

        """

        # On ignore les erreurs au niveau du site
        # pour éviter les latences.
        try:

            # On crée un article avec les données
            # trouvées sur l'article en ligne.
            article = Article(

                id_site=self.site['id'],

                title=response.css(self.site['title']).get(),

                description="".join(response.css(

                    self.site['content']).getall()),

                category="".join(response.css(

                    self.site['category']).getall()),

                author=response.css(self.site['author']).get(),

                published_at=response.css(self.site['published_at']).get(),

                url=response.url,

            )

            # On insère l'article dans la base de données.
            db.execute(article.insert())

        except Exception:

            # S'il y a une exception au niveau du site,
            # on l'ignore.
            pass
