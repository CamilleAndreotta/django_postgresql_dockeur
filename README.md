# django_postgresql_dockeur
Template de projet Python/Django avec une base Postgesql dockeurisé 

## Installation du projet 

Copier le .env.exemple en .env
Modifier les variables d'environnement. Pour le POSTGRES_HOST la valeur est db (nom du service dans le docker-compose.yml)

## Les commandes 

```
Création des migrations
docker compose exec app python manage.py makemigrations

Lancement des migrations
docker compose exec app python manage.py migrate
```
