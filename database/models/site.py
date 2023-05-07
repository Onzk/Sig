"""
Le module database.models.site contient 
la représentation en classe, de la table 'sites'
de la base de données.

"""

from pydantic import BaseModel


class Site(BaseModel):
    """
    Cette classe représente la table 'sites'
    dans la base de données.

    """

    # Définit le nom courrant du site.
    name: str

    # Définit l'url du site.
    url: str

    def prepare(self):
        """
        Cette fonction est chargée de d'épurer les valeurs
        des attributs de l'objet courrant.

        """
        self.name = self.name.replace("'", "\\'").strip()

        self.url = self.url.replace("'", "\\'").strip()

    @staticmethod
    def select(id=None):
        """
        Cette fonction renvoie le script SQL 
        pour récupérer tous les sites, ou un seul, si 
        un identifiant est indiqué, depuis la 
        base de données.

        """
        query = f"""SELECT * FROM sites"""

        return query if id == None else f"""{query} WHERE id={id}"""

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

            INSERT INTO sites(name, url) 

                VALUES('{self.name}','{self.url}')

            """

    def update(self, id: int):
        """
        Cette fonction renvoie le script SQL 
        pour mettre à jour un site dont l'identifiant est
        spécifié, dans la base de données.

        """

        # On épure les valeurs des attributs de l'objet.
        self.prepare()

        # On retourne un script SQL pour la modification
        # d'un site avec les informations contenues
        # dans les attributs de l'objet, dans la base de données.
        return f"""

            UPDATE sites 

                SET name='{self.name}', url='{self.url}' 

                WHERE id={id}

            """

    @staticmethod
    def delete(id: int):
        """
        Cette fonction renvoie le script SQL 
        pour supprimer un site dont l'identifiant est
        spécifié, dans la base de données.

        """
        return f"""

            DELETE FROM sites 

                WHERE id={id}

            """
