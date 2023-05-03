# prepas-scientifiques
Projet 1G5 NSI Elouan Deschamps, recolte et triage de données concernant les prépas scientifiques

Ce projet consiste en une interface permettant de trouver et d'afficher des données par établissement concernant les prépas scientifiques disponibles sur parcoursup.

## Framework utilisés
Cette application sera utilisable dans un navigateur Web et utilisera:
* Html
* Css
* Python
* Django

## Objectifs
### Triage de données
Il faudra trier les données en fonction de:
* Fillière
* Types de Bachelier admissible
* Département
* Académie
* Ville
* Internat ou non

### Affichage des données
Données concernant les formations qui seront affichées dans l'interface:
* Fillière
* Taux d'accessibilité 
* Position sur une carte
* Places disponibles
* Places en internat disponibles
* Lien vers la fiche formation de l'établissement

## Problèmes
Avec le fichier csv:
* Certaines prépas sont hors cadres et ont un intilué différent des fillières traditionelles.
* Certaines cases sont vides

Avec le raspberry-pi:
* Le module python ssl n'a pas pu être compilé à cause de la version de openssl (1.1.1), il faudrait compiler openssl, passer en debian testing ou sur fedora
