# Projet Wikidata

Ce projet a été conçu pour être exécuté dans un environnement Python 3.11. Suivez ces étapes pour mettre en place l'environnement de développement.

## Instructions d'Installation

1. **Création de l'environnement virtuel (venv):**

   ```bash
   python3.11 -m venv venv
   ```

   Activez l'environnement virtuel :

   - Sur Windows (cmd) :
     ```bash
     .\venv\Scripts\activate
     ```
   - Sur macOS/Linux :
     ```bash
     source venv/bin/activate
     ```

2. **Installation des bibliothèques requises :**

   Assurez-vous d'avoir activé votre environnement virtuel, puis installez les bibliothèques nécessaires à l'aide de pip :

   ```bash
   pip install django matplotlib requests
   ```

## Démarrage du Serveur

1. Ouvrez un terminal dans le répertoire du projet.

2. **Lancer le serveur web :**

   ```bash
   python manage.py runserver
   ```

3. Accédez à votre navigateur et entrez l'adresse suivante :
   ```plaintext
   http://127.0.0.1:8000/
   ```

Ces étapes vous permettront de créer un environnement virtuel, d'installer les bibliothèques nécessaires, et de démarrer le site web localement. Explorez le projet et contribuez selon vos besoins.
