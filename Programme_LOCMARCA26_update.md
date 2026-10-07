# Programme préliminaire LOCMARCA 26

#### [https\://github.com/gcambon/script-locmarca](https://github.com/gcambon/script-locmarca) 

---

**Jour 1 Lundi**  
Matin

* Accueil \- présentation des participants (1 slide / person; pdf à envoyer avant)  
* Présentation du programme cours-tp  
* Infrastructure de travail \- kabre et jupyterhub ondemand (=\> gérer ouverture comptes Kabré)


Après-midi  
**TP 0  (avec README du github) : installation**

* connexion Kabre \+ jupyterhub  
* installation de MobaXterm pour les utilisateurs sous Windows \+ connexion (ssh \-X …)  
* environnement python et module

---

**Jour 2 \- Mardi**   
**Cours 1** : Présentations des produits d’observation : In situ versus satellites

* ocean / atmo / bgc   
* 2D versus 3D  
* couverture spatio-temporelle, limites et avantages  
* expliquer ce qu’est les données climato versus interannuelles variabilité  
* données grillées : ça implique quoi ? ;  interpolation, leurs limites

**Cours 2a** : C’est quoi un fichier netcdf et son “anatomie”

**Cours 2b** : Courte intro a l'utilisation de ncview avec le terminal

**TP 1a** : bases de xarray (ouvrir un fichier netCDF, sélectionner, moyenner, cartes)

**TP 1b** : sur les obs : avec des données déjà dispo sur kabre 

* Carte 2D-h, section verticale etc…, séries temporelles  
* Introduction outils NCO / CDO vs. python

**TP 2a** : Comment on récupère des données  : copernicus/ecmwf

* exo 0 :compte copernicus /ecmwf  
* exo 1 :    
  * récupérer données par SST L4 \+ temperature 3D sur zone costa rica  
  * plot sur une zone de leur choix.  
* exo 2 : même chose pour réanalyse atmo (vent), réanalyse ocean (temp, salt et courant) 

---

**Jour 3 \- Mercredi**  
**TP 2b / TP 2c** (compléments, placement à décider) :

* TP 2b : biogéochimie (chlorophylle satellite, nitrate et oxygène modèle, zone de minimum d'oxygène)  
* TP 2c : climatologie vs variabilité interannuelle (31 ans de SST, anomalies, El Niño / La Niña)

**Cours 3 :** on a vu les données d’observation hier, aujoud’hui modèle

* c’est quoi un modèle numérique d'océan / atmo / climat  
* *Principe & grandes idées à avoir :*   
* *Résolution spatiale / intégration / processus / type de grille*  
* *A quoi ça sert (étude de processus)*  
* *global vs régional, scénarios, limites*  
* *Présentation succincte modèles climats : lien possible https\://esgf-node.ipsl.upmc.fr/projects/esgf-ipsl/*

**TP 3** : visu et manipulation sortie de **modèle océan**

* lecture/ouverture/carte avec données dispo sur cluster avec CROCO et NEMO GLOBAL 1° avec BGC  
* données 2D SST / SLA / Vents /  Courants de surface.   
* données 3D : température, salinité, Courant  
  * carte et section verticale

---

**Jour 4 \- Jeudi \-  Objectif mini-projet :** mini-projet simple sur une zone choisie de comparaison modèle-données  
**TP 4 :**

* Définir région d'intérêt  
* Récupération données in-situ / sat / réanalyse océan et atmo / sorties modèles océan   
* Validation et comparaison modèles/observations  
* Cycle saisonnier et variabilité interannuelle pour ces données 

---

**Jour 5 \- Vendredi**

* Finish  
* Tour de table \- présentation en 5 slides   
* Restitution / récupération éventuelle des données


Après-midi :  

* ???