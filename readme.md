# Sig : Scrapeur d'articles en ligne
![scrapy logo image](https://upload.wikimedia.org/wikipedia/fr/1/16/Scrapy_logo.png)

[![pyversions](https://img.shields.io/pypi/pyversions/scrapy-playwright.svg)](https://pypi.python.org/pypi/scrapy-playwright)

## A propos

Sig est un programme basé sur [Scrapy](https://github.com/scrapy/scrapy) permettant
de récupérer des articles en ligne et de les insérer dans une base de données.

Il est facilement configurable et adapté pour prendre en compte, l'ajout de nouveaux
sites de news où trouver des articles.

Ce projet a été réalisé dans le cadre scolaire par des étudiants. 

Université : Université Catholique de l'Afrique de l'Ouest - Unité Universitaire du Togo ([UCAO-UUT](https://ucao-uut.tg/)).

Professeur en charge : Mr ANAKPA Manawa

Cours : Programmation python

Institu : Institut Supérieur des Technologies Informatiques et Numériques (ISTIN)

Parcours : Développement d'applications - Licence 3

Année scolaire : 2022-2023 


## Requis

Le programme peut tout aussi bien fonctionner sous Windows comme sous un système Linux.


### Minimum requis pour les versions

* python >= 3.11.2
* scrapy >= 2.8.0
* fastApi >= 0.95.1
* uvicorn >= 0.22.0
* mysql-connector-python >= 8.0.33
* lxml >= 4.9.2


## Installation

Pour pouvoir utiliser cette application, vous aurez besoin de certains modules python.


### - Installation rapide

Pour une installation rapide de tous les modules dont vous aurez besoin, placez-vous à la racine du projet et faites :

```
pip install -r requirements.txt
```

### - Installation progressive

Pour une installation progressive de tous les modules dont vous aurez besoin, tapez les commandes suivantes pour installer :

* `scrapy` qui est disponible sur PyPI et peut être installé avec `pip`:

```
pip install scrapy
```

* `fastApi` qui est disponible sur PyPI et peut être installé avec `pip`:

```
pip install fastapi[all]
```

* `uvicorn` qui est disponible sur PyPI et peut être installé avec `pip`:

```
pip install uvicorn
```

* `mysql-connector-python` qui est disponible sur PyPI et peut être installé avec `pip`:

```
pip install mysql-connector-python
```

* `lxml` qui est disponible sur PyPI et peut être installé avec `pip`:

```
pip install lxml
```

## Configuration

Avant de lancer l'application, vous devez premièrement la configurer. Pour cela, rendez-vous dans le fichier `config/config.py`.

Vous devez d'abord créer manuellement une [base de données](https://www.oracle.com/fr/database/comment-creer-base-donnees-mysql.html).

Définissez la base de données où vous voulez stocker les données.
```python
DB_NAME = "dbname"
```

Modifier le nom d'utilisateur avec lequel vous vous connectez à la base de données.
```python
DB_USER = "root"
```

Modifier le mot de passe de l'utilisateur avec lequel vous vous connectez à la base de données.
```python
DB_PASSWORD = ""
```

Modifier l'hôte sur lequel se trouve la base de données.
```python
DB_HOST = "localhost"
```

## Lancement

Pour lancer l'application (sous Windows/Linux), entrez la commande suivante dans le terminal.
```
python -m uvicorn web:app
```

Pour lancer l'application en mode rafraîchissement au changement de fichier, entrez la commande suivante dans le terminal.
```
python -m uvicorn web:app --reload
```

Plus d'informations sont disponibles sur le lancement d'une application faite avec [`FastApi`](https://fastapi.tiangolo.com/tutorial/first-steps/).


## Utilisation basique

Après avoir [lancé l'application](#lancement), vous pouvez effectué des requêtes avec votre testeur de api (`Postman`, `Insomnia`, etc...).

L'api démarre sur une adresse lors du lancement.
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Vous devez ajouter `/docs` au lien pour accéder à la documentation de l'api et savoir comment elle fonctionne.
