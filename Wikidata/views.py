from django.shortcuts import render
import requests
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

# Create your views here.
def home(request):
    global coteG, coteGd
    valeurs = None
    url = "http://localhost:7200/repositories/PROJECT"
    query = """
    PREFIX riedel: <https://cours.iut-orsay.fr/npbd/projet/riedel/> 
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
    PREFIX owl: <http://www.w3.org/2002/07/owl#> 
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
    PREFIX iut: <https://cours.iut-orsay.fr/qar/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX wd: <http://www.wikidata.org/entity/>
    PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    PREFIX wikibase: <http://wikiba.se/ontology#>
    
    SELECT DISTINCT *  WHERE{
        ?item rdf:type riedel:Personnage;
              riedel:nom ?nom;
              riedel:revenu ?revenu;
              riedel:cote ?cote;
              riedel:genre ?Genre;
    }
    """

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/sparql-results+json",
    }

    params = {
        "query": query,
        "format": "json",  # Vous pouvez changer le format de sortie selon vos besoins
    }
    nb = None
    base64_image = None
    try:
        # Faire la requête GET avec les paramètres spécifiés
        response = requests.get(url, headers=headers, params=params)

        # Vérifier si la requête a réussi (code 200)
        if response.status_code == 200:
            # Afficher la réponse JSON
            value = response.json()
            valeurs = []
            cote = {
                'Gentil': [0,[]],
                'Méchant': [0,[]],
                'Neutre': [0,[]]
            }
            coteG = {
                'féminin': [0,0],
                'masculin': [0,0],
                'agenre': [0,0],
                'mâle' : [0,0],
                'genre-fluide' : [0,0],
                'hermaphrodisme' : [0,0],
                'femelle' : [0,0],
            }
            coteGd = {
                'féminin': 0,
                'masculin': 0,
                'agenre': 0,
                'mâle': 0,
                'genre-fluide': 0,
                'hermaphrodisme': 0,
                'femelle': 0,
            }
            value = value["results"]["bindings"]
            for i in value:
                valeurs.append([i['nom']["value"], i['cote']['value'],i['Genre']['value'], i['revenu']['value']])
                cote[i['cote']['value']][0] += 1
                cote[i['cote']['value']][1].append(int(i['revenu']['value']))
                coteG[i['Genre']['value']][0]+=int(i['revenu']['value'])
                coteG[i['Genre']['value']][1] += 1
                coteGd[i['Genre']['value']] += 1

            x = ["féminin","masculin","agenre","genre-fluide","hermaphrodisme"]
            y = [
                coteG['féminin'][0]/coteG['féminin'][1] + coteG['femelle'][0]/coteG['femelle'][1],
                coteG['masculin'][0]/coteG['masculin'][1] + coteG['mâle'][0]/coteG['mâle'][1],
                coteG['agenre'][0]/coteG['agenre'][1],
                coteG['genre-fluide'][0]/coteG['genre-fluide'][1],
                coteG['hermaphrodisme'][0]/coteG['hermaphrodisme'][1]
            ]

            print(coteG)
            plt.bar(x, y)
            image_stream = BytesIO()
            plt.savefig(image_stream, format='png')
            image_stream.seek(0)
            base64_image = base64.b64encode(image_stream.read()).decode('utf-8')

            nb = {
                'Gentil': cote['Gentil'][0],
                'Méchant': cote['Méchant'][0],
                'Neutre': cote['Neutre'][0]
            }
            plt.close()
        else:
            # Afficher un message d'erreur si la requête a échoué
            print(f"Erreur: {response.status_code}\n{response.text}")

    except requests.exceptions.RequestException as e:
        # Gérer les erreurs de requête
        print(f"Erreur de requête: {e}")

    return render(request, 'home.html', {"plot" : base64_image, "valeurs": valeurs, "cote": coteGd})
