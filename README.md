# Projet Wikidata

Ce projet a été conçu pour être exécuté dans un environnement Python 3.11. Suivez ces étapes pour mettre en place l'environnement de développement.

## Instructions d'Installation

1. **Création de l'environnement virtuel (venv):**

   ```bash
   python -m venv venv
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

3. **Configuration de la partie GraphDB :**

   - Ajoutez l'ontologie `nicolas.ttl` et les déclarations `statements.ttl` dans un référentiel nommé "PROJECT".

4. **Démarrage du Serveur**

   - Ouvrez un terminal dans le répertoire du projet.

   - **Lancer le serveur web :**

     ```bash
     python manage.py runserver
     ```

   - Accédez à votre navigateur et entrez l'adresse suivante :
     ```plaintext
     http://127.0.0.1:8000/
     ```

Ces étapes vous permettront de créer un environnement virtuel, d'installer les bibliothèques nécessaires, et de démarrer le site web localement. Assurez-vous également d'ajouter les fichiers d'ontologie et de déclarations dans le référentiel "PROJECT" pour la partie GraphDB.
