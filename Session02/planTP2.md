# Plan — TP2 « Comment on récupère des données : Copernicus »

## Contexte

Le TP3 du mardi (programme LOCMARCA 26, [Programme_LOCMARCA26_update.pdf](script-locmarca/Programme_LOCMARCA26_update.pdf)) n'existe pas encore. Il vient après le TP2 (données déjà présentes sur Kabre) : cette fois, les étudiants **récupèrent eux-mêmes** des données, puis les tracent. Au programme :
- exercice 0 : compte Copernicus ;
- exo 1 : SST L4 + température 3D sur la zone Costa Rica, puis tracé sur une zone de leur choix ;
- exo 2 : même démarche pour la réanalyse atmo (vent) et la réanalyse océan (T, S, courants).

Choix déjà validés :
- **tout via Copernicus Marine** (`copernicusmarine.subset()`), avec ERA5/CDS seulement en 🚀 Advanced track ;
- **rangement dans `Session01/`**, à côté du TP2.

On a de la matière brute à réutiliser : [download_sst.ipynb](script-locmarca/my-notebooks/ocean/download_sst.ipynb), [download_3d_ocean_bymonth.ipynb](script-locmarca/my-notebooks/ocean/download_3d_ocean_bymonth.ipynb) et [plot_sst_central_america.ipynb](script-locmarca/my-notebooks/ocean/plot_sst_central_america.ipynb). On y reprend le motif « skip si le fichier existe + `subset()` » ainsi que la fonction `base_map`.

## Datasets (vérifiés dans le catalogue via `copernicusmarine.describe`)

Zone Costa Rica : lon −92 → −80, lat 4 → 14. Elle couvre le golfe de Papagayo, le dôme du Costa Rica et la côte caraïbe.

| Usage | dataset_id | Variables | Fenêtre proposée |
|---|---|---|---|
| Exo 1a : SST L4 (sat) | `METOFFICE-GLO-SST-L4-REP-OBS-SST` (OSTIA, 0.05°, journalier) | `analysed_sst` (K) | janv.→mars 2023 |
| Exo 1b : T 3D **observée** | `cmems_obs-mob_glo_phy_my_0.125deg_P1M-m` (ARMOR3D, sat + in situ, mensuel, jusqu'à 2024-12) | `to`, `so` | 2023, 0–500 m |
| Exo 2a : réanalyse océan | `cmems_mod_glo_phy_my_0.083deg_P1M-m` (GLORYS12, mensuel) | `thetao`, `so`, `uo`, `vo` | janv.→mars 2023, 0–500 m (13 Mo, contre 50 Mo pour l'année entière ; même période que l'exo 1a) |
| Exo 2b : vent (ERA5 corrigé par scatteromètres) | `cmems_obs-wind_glo_phy_my_l4_0.125deg_PT1H` (horaire) | `eastward_wind`, `northward_wind` | 1→31 janv. 2023 |

Ce choix a un intérêt pédagogique :
- janvier–mars correspond à la saison du **jet de Papagayo**. Le vent de l'exo 2 explique la langue d'eau froide vue dans la SST de l'exo 1, ce qui fait le lien entre les deux exercices ;
- ARMOR3D (observations interpolées) et GLORYS (modèle + assimilation) mesurent la même grandeur. Les comparer introduit la notion « obs vs modèle » du mercredi et du jeudi.

## Structure du notebook (solution)

0. **Intro** : comment travailler dans le notebook (même bloc que le TP2), puis rappel du Cours 1 (L4 = grillé/interpolé, obs vs réanalyse).
1. **Exo 0 — Compte et login** : créer un compte sur marine.copernicus.eu, puis lancer `copernicusmarine login` **dans un terminal** (jamais de mot de passe dans le notebook). Vérification dans le notebook avec `copernicusmarine.login(check_credentials_valid=True)` (API Python plutôt que `!copernicusmarine`, qui n'est pas toujours dans le PATH du kernel).
2. **Trouver un dataset** : lire une page produit, puis `copernicusmarine.describe(dataset_id=...)` pour lister les variables, les unités et la couverture temporelle. Cheat-sheet des arguments de `subset()`. Une petite fonction `download(fname, **kwargs)` (skip si le fichier existe, `DATA_DIR = Path("data_tp3")`) est fournie toute faite aux étudiants. Elle refuse de partir si un argument vaut encore `...` (TODO non rempli) et, si le téléchargement échoue, se replie sur la copie de secours `OBS_DIR/TP3_BACKUP/`.
3. **Exo 1a — SST L4** : `subset` à trous (dataset, variable, box, dates), puis ouverture et `print(ds)`. Carte de la moyenne en °C avec `base_map`, puis carte de la SST d'un jour de janvier.
   - ✅ Check : taille du fichier, dimensions, valeurs entre ~23,5 et 30 °C, langue froide au large de Papagayo (< 22 °C le 16 janvier 2023, jour choisi pour la carte journalière).
4. **Exo 1b — Température 3D (ARMOR3D)** : `subset` avec `minimum_depth`/`maximum_depth`, carte à 100 m, section verticale à 9°N (axe inversé, isotherme 20 °C). On prend 9°N plutôt que 10°N parce que le dôme y est plus net.
   - ✅ Check : thermocline peu profonde, qui remonte vers le dôme du Costa Rica (isotherme 20 °C vers 30 m à 89°W, ~60 m près de la côte).
5. **Vérification croisée** : moyenne de la SST OSTIA vs moyenne de `to` en surface ARMOR3D sur la même boîte et la même période. Puis comparaison mois par mois (OSTIA ramené en moyennes mensuelles avec `resample(time="MS")`). Écart mesuré : −0,06 °C sur la boîte, moins de 0,1 °C par mois. On discute pourquoi ce n'est pas identique : résolution, masques terre, SST de « fondation » vs niveau 0 m. Et on se demande si les deux méthodes sont vraiment indépendantes, puisque ARMOR3D utilise la SST satellite en entrée.
6. **Exo 1c — Votre zone** : l'étudiant remplit des variables `MY_LON_MIN…MY_LAT_MAX` et `MY_NAME` (le nom du fichier), relance la SST sur janv.→mars 2023, puis trace la carte (`base_map` prend un argument `extent`). On utilise des variables séparées pour ne pas modifier la boîte Costa Rica, dont les exos suivants ont besoin. Exemple dans la solution : le golfe de Tehuantepec, autre jet de trouée, avec sa langue froide à ~26 °C.
   - ✅ Check sur la taille : garder une boîte de moins de 15°×15°, ce que vérifie un `assert` (~7 Mo pour 10°×10°).
7. **Débogage volontaire** : un appel direct à `copernicusmarine.subset()` qui doit récupérer « la première semaine de l'enregistrement OSTIA ». Il contient deux bugs : des dates en 1980, alors que la couverture commence le 1981-10-01 (`CoordinatesOutOfDatasetBounds`, qui apparaît en premier), et `variables=["sst"]` au lieu de `analysed_sst` (`VariableDoesNotExistInTheDataset`). L'étudiant lit la dernière ligne de chaque erreur, puis corrige grâce à `show_dataset`. On prend une date antérieure au début de l'enregistrement parce qu'elle restera fausse en 2027 et 2028, contrairement à la fin de couverture, qui avance.
8. **Exo 2a — Réanalyse océan GLORYS** : `subset` avec 4 variables. Carte de la SST modèle avec les courants de surface (`quiver` sous-échantillonné) et section T/S à 9°N (même latitude que l'exo 1b).
   - ✅ Check : sens des courants, avec le contre-courant nord-équatorial vers l'est à 7–8°N et un flux vers l'ouest à 10–11°N, qui forment une boucle autour du dôme.
9. **Exo 2b — Vent** : `subset` horaire, puis `resample(time="1D").mean()`, puis carte de la vitesse moyenne de janvier avec les flèches.
   - ✅ Check : jet de Papagayo d'environ 10 m/s (maximum 10,4 m/s en moyenne de janvier), orienté vers l'ouest-sud-ouest, au-dessus de la langue froide de l'exo 1a.
10. **🚀 Advanced tracks** :
    - (A) section ARMOR3D vs GLORYS côte à côte avec leur différence : un avant-goût du jeudi. GLORYS ne couvrant que janv.→mars, on restreint ARMOR3D aux mêmes mois ;
    - (B) superposer les contours de SST OSTIA sur la carte de vent (lien vent-upwelling) ;
    - (C) ERA5 via ECMWF CDS (`cdsapi`, compte + licence), présenté en cellules commentées avec l'avertissement sur la file d'attente.
11. **Récap** : tableau des 4 datasets (type obs/réanalyse, résolution, fréquence) et rappel que les fichiers sont gardés pour le mini-projet du jeudi.

La **version étudiant** remplace par des trous les arguments de `subset`, les sélections `.sel`/`.mean` et la conversion K→°C. Les imports, `download()`, `base_map` et la mise en forme des figures restent complets.