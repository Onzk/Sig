"""
Le module database.models.article contient 
la représentation en classe, de la table 'articles'
de la base de données.

"""

from tools import html_clean


class Article():
    """
    Cette classe représente la table 'articles'
    dans la base de données.

    """

    # Définit l'identifiant du site de provenance
    id_site: int

    # Définit le titre de l'article
    title: str

    # Définit l'url de l'article
    url: str

    # Définit le contenu de l'article
    description: str

    # Définit la catégorie de l'article
    category: str

    # Définit l'auteur de l'article
    author: str

    # Définit l'heure de publication de l'article
    published_at: str

    def __init__(self, id_site: int, title: str, url: str, description: str, category: str, author: str, published_at: str) -> None:
        """
        Cette fonction est le constructeur de la classe.

        """
        self.id_site = id_site

        self.title = title

        self.url = url

        self.description = description

        self.category = category

        self.author = author

        self.published_at = published_at

    def prepare(self):
        """
        Cette fonction est chargée d'épurer les valeurs
        des attributs de l'objet courrant.

        """
        self.title = html_clean(self.title)

        self.url = html_clean(self.url)

        self.description = html_clean(self.description)

        self.category = html_clean(self.category)

        self.author = html_clean(self.author)

        self.published_at = html_clean(self.published_at)

    @staticmethod
    def select(field=None, slug=None, operator="="):
        """
        Cette fonction renvoie le script SQL 
        pour récupérer tous les articles, ou un seul, si 
        un identifiant est indiqué, depuis la
        base de données.

        """
        query = f"""
        
            SELECT articles.id, name, title, articles.url, description,
                
                category, author, published_at, articles.created_at 

                FROM articles, sites 

                WHERE sites.id = articles.id_site

            """

        return query if field == None else f"""{query} AND {field} {operator} {slug}"""

    def insert(self):
        """
        Cette fonction renvoie le script SQL 
        pour insérer les valeurs de l'objet courrant
        dans la base de données.

        """

        # On épure les valeurs des attributs de l'objet.
        self.prepare()

        # On retourne un script SQL pour l'insertion des informations
        # contenues dans les attributs de l'objet dans la base de données.
        return f"""
    
            INSERT INTO articles(id_site, title, url, description, category, author, published_at, created_at) 

                VALUES({self.id_site}, '{self.title}','{self.url}', 
                
                    '{self.description}','{self.category}',
                
                    '{self.author}', '{self.published_at}', NOW()

                )

            """

    @staticmethod
    def delete(id: int):
        """
        Cette fonction renvoie le script SQL 
        pour supprimer un articles de 
        la base de données avec l'identifiant id.

        """
        return f"""
            
            DELETE FROM articles WHERE id = {id}
            
            """
