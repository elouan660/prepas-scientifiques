# prepas-scientifiques
Projet 1G5 NSI Elouan Deschamps, recolte et triage de données concernant les prépas scientifiques

Ce projet consiste en une interface permettant de trouver et d'afficher des données par établissement concernant les prépas scientifiques disponibles sur parcoursup.

## Frameworks utilisés
Cette application sera utilisable dans un navigateur Web et utilisera:
* Html
* Css
* Python
* Django
* Javascript
* Leaflet

## Objectifs
### Triage de données
Il faudra trier les données en fonction de:
* Filière
* Types de Bachelier admissible
* Département
* Académie
* Ville
* Internat ou non
* Public ou non

### Affichage des données
Données concernant les formations qui seront affichées dans l'interface:
* Filière
* Taux d'accessibilité 
* Position sur une carte
* Places disponibles
* Places en internat disponibles
* Lien vers la fiche formation de l'établissement
* Statistiques générales dans des graphiques

## Problèmes
Avec le fichier csv:
* Certaines prépas sont hors cadres et ont un intitulé différent des fillières traditionelles.
* Certaines filières traditionnelles incluent des précisions dans le nom de la fillière
* Certaines cases parfois sont vides, parfois sans raison apparente
* Beaucoup de données inutiles sont incluses dans le csv

