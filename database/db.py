"""
Le module database.db contient 
la représentation tout ce qu'il faut pour
interargir avec la base de données.

"""

import mysql.connector

import config.config as config


# On crée un lien avec la base données, 
# depuis les paramètres configurés.
mysqldb = mysql.connector.connect(

    host=config.DB_HOST,

    user=config.DB_USER,

    password=config.DB_PASSWORD,

    database=config.DB_NAME

)

# On définit un objet pour exécuter les
# commandes SQL.
connexion = mysqldb.cursor()


def execute(query: str):
    """
    Cette fonction est chargée d'éxécuter
    une commande SQL.

    """

    # On enlève les espaces au début
    # et à la fin de la commande.
    query = query.strip()
    
    # On rafraîchit la connexion 
    # à la base de données.
    mysqldb.reconnect()
    
    # On rétablit le curseur.
    connexion = mysqldb.cursor()

    # On exécute la commande.
    connexion.execute(query)

    # Si la commande est un 'SELECT',
    if query.startswith('SELECT'):

        # on récupère les données trouvées dans
        # la base de données.
        return connexion.fetchall()

    # Sinon, on valide les opérations
    # faites par la commande SQL.
    return mysqldb.commit()


def rollback():
    """
    Cette fonction est chargée d'annuler
    une opération faite par une commande 
    SQL.

    """
    mysqldb.rollback()


def init():
    """
    Cette fonction est chargée de créer
    les tables 'sites' et 'articles' si elles
    n'existent pas (cas d'une première utilisation).

    """

    # On ouvre le fichier contenant le script
    # de la création de la table 'sites'.
    with open("database/scripts/create_sites.sql", "r") as script:

        # On exécute le contenu du fichier
        connexion.execute(script.read())

    # On ouvre le fichier contenant le script
    # de la création de la table 'articles'.
    with open("database/scripts/create_articles.sql", "r") as script:

        # On exécute le contenu du fichier
        connexion.execute(script.read())
