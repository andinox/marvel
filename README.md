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


## INSERT SPARQL

```js
PREFIX riedel: <https://cours.iut-orsay.fr/npbd/projet/riedel/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema>
PREFIX iut: <https://cours.iut-orsay.fr/qar/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wikibase: <http://wikiba.se/ontology>
PREFIX : <http://www.semanticweb.org/nriedel/ontologies/2023/11/untitled-ontology-3/>


INSERT {
    ?item rdf:type riedel:Personnage ;
        riedel:genre ?Genre.
} 
WHERE {
  ?item rdf:type riedel:Personnage ;
        riedel:nom ?nom .

  SERVICE <https://query.wikidata.org/bigdata/namespace/wdq/sparql> {
    ?itemWikidata wdt:P31 wd:Q1114461;
        wdt:P1080 ?universe;
          rdfs:label ?itemWikidataLabel;
        wdt:P21 ?genre.
    ?genre rdfs:label ?genreLabel.
        FILTER(?universe = wd:Q931597)
        FILTER(LANG(?itemWikidataLabel) = "fr")
        FILTER(LANG(?genreLabel) = "fr")
  }
    FILTER(?nom = ?itemWikidataLabel)
    BIND(?genreLabel AS ?Genre)
} 
```