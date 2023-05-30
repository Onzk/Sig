"""
#####################################################"
Le module web contient l'api de l'application.
Il s'agit du point d'encrage et de lancement du
programme.
#####################################################"
LANCEMENT : python -m uvicorn web:app
#####################################################"
AUTEURS : 
    - AMON Anne-Emmanuella Naomi Ahou,
    - KOUDOSSOU Messan Dhani Justin.
#####################################################"
GROUPE : Numéro 8.
#####################################################"

"""

from fastapi import FastAPI

from database.models.article import Article

from database.models.site import Site

import database.db as db

import app.crawler as crawler

# On démarre l'api.
app = FastAPI()

# On initialise la base données.
db.init()

# On lance le scraping une fois.
crawler.crawl()


@app.get('/sites')
async def sites_index():
    """
    Cette route est chargée de récupérer tous les
    sites de la base de données.

    """
    try:
        # On récupère tous les sites dans la base de données.
        data = db.execute(Site.select())

        # On affiche la liste des sites.
        return {"success": True, "data": data}

    except Exception as e:

        # On annule les changements, en cas d'erreur.
        db.rollback()

        # On renvoie le message d'erreur, en cas d'erreur.
        return {"success": False, "data": {}, "error": e}


@app.post('/sites')
async def sites_store(site: Site):
    """
    Cette route est chargée d'insérer un
    site dans la base de données.

    """
    try:

        # On insère le site dans la base de données.
        db.execute(site.insert())

        # On renvoie les informations fournies
        # pour créer le site.
        return {"success": True, "data": site}

    except Exception as e:

        # On annule les changements, en cas d'erreur.
        db.rollback()

        # On renvoie le message d'erreur, en cas d'erreur.
        return {"success": False, "data": site, "error": e}


@app.put('/sites/{id}')
async def sites_update(site: Site, id: int):
    """
    Cette route est chargée de mettre à jour 
    un site existant dans la base de données.

    """
    try:

        # On met à jour le site.
        db.execute(site.update(id))

        # On renvoie les informations fournies
        # pour mettre à jour le site.
        return {"success": True, "data": site}

    except Exception as e:

        # On annule les changements, en cas d'erreur.
        db.rollback()

        # On renvoie le message d'erreur, en cas d'erreur.
        return {"success": False, "data": site, "error": e}


@app.delete('/sites/{id}')
async def sites_detele(id: int):
    """
    Cette route est chargée de supprimer 
    un site existant de la base de données.

    """
    try:

        # On supprime le site.
        db.execute(Site.delete(id))

        # On renvoie les informations fournies
        # pour supprimer le site.
        return {"success": True, "data": id}

    except Exception as e:

        # On annule les changements, en cas d'erreur.
        db.rollback()

        # On renvoie le message d'erreur, en cas d'erreur.
        return {"success": False, "data": id, "error": e}


@app.get('/sites/{id}')
async def sites_show(id: int):
    """
    Cette route est chargée de récupérer
    un site existant dans la base de données.

    """
    try:

        # On récupère le site.
        data = db.execute(Site.select(id))

        # On renvoie les informations du site.
        return {"success": True, "data": data}

    except Exception as e:

        # On renvoie le message d'erreur, en cas d'erreur.
        return {"success": False, "data": data, "error": e}


@app.get('/scrap')
async def articles_scrap():
    """
    Cette route est chargée de lancer le 
    webscraping, sur les sites stockés dans 
    la base de données et configurés
    dans le programme.

    Elle représente le coeur du programme.

    """
    return {"success": True, "data": crawler.crawl()}


@app.get('/articles')
async def articles_index():
    """
    Cette route est chargée de récupérer tous
    les articles qui sont dans la base de données.

    """
    try:

        # On récupère les articles.
        data = db.execute(Article.select())

        # On renvoie les articles récupérés.
        return {"success": True, "count": len(data),  "data": data}

    except Exception as e:

        # On annule les changements, en cas d'erreur.
        db.rollback()

        # On renvoie le message d'erreur, en cas d'erreur.
        return {"success": False, "data": {}, "error": e}


@app.get('/articles/category/{category}')
async def articles_category(category: str):
    """
    Cette route est chargée de récupérer tous
    les articles qui sont dans la base de données
    et appartenant à une catégorie.

    """
    try:

        # On récupère les articles, appartenant à la catégorie
        # spécifiée dans l'url.
        data = db.execute(Article.select(
            field="category",
            operator="LIKE",
            slug=f"'%{category}%'"))

        # On renvoie les articles récupérés.
        return {"success": True, "count": len(data), "data": data}

    except Exception as e:

        # On annule les changements, en cas d'erreur.
        db.rollback()

        # On renvoie le message d'erreur, en cas d'erreur.
        return {"success": False, "data": {}, "error": e}


@app.get('/articles/author/{author}')
async def articles_author(author: str):
    """
    Cette route est chargée de récupérer tous
    les articles qui sont dans la base de données
    et publiés par un auteur.

    """
    try:

        # On récupère les articles,
        # publiés par un auteur.
        data = db.execute(Article.select(
            field="author",
            operator="LIKE",
            slug=f"'%{author}%'"))

        # On renvoie les articles récupérés.
        return {"success": True, "count": len(data), "data": data}

    except Exception as e:

        # On annule les changements, en cas d'erreur.
        db.rollback()

        # On renvoie le message d'erreur, en cas d'erreur.
        return {"success": False, "data": {}, "error": e}


@app.get('/articles/site/{id}')
async def articles_site(id: int):
    """
    Cette route est chargée récupérer tous
    les articles qui sont dans la base de données
    et provenant d'un site spécifique.

    """
    try:

        # On récupère les articles, 
        # provenant du site spécifié.
        data = db.execute(Article.select(
            field="id_site",
            operator="=",
            slug=id))

        # On renvoie les articles récupérés.
        return {"success": True, "count": len(data), "data": data}

    except Exception as e:

        # On annule les changements, en cas d'erreur.
        db.rollback()

        # On renvoie le message d'erreur, en cas d'erreur.
        return {"success": False, "data": {}, "error": e}


@app.delete('/articles/{id}')
async def articles_delete(id: int):
    """
    Cette route est chargée de supprimer 
    un article dans la base de données.

    """
    try:

        # On supprime l'article.
        db.execute(Article.delete(id))

        # On renvoie que tout s'est bien passé.
        return {"success": True, "data": None}

    except Exception as e:

        # On annule les changements, en cas d'erreur.
        db.rollback()

        # On renvoie le message d'erreur, en cas d'erreur.
        return {"success": False, "data": None, "error": e}
