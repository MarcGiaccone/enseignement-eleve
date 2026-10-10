---
titre: Retoucher une photo
titre_page: "TP SNT : retoucher une photo"
surtitre: SNT · Seconde · Travaux pratiques
intro: "Redresser, recadrer, réduire les couleurs : trois transformations de base pour comprendre ce qui change dans une image numérique."
meta:
  - En binôme
  - Logiciel GIMP 3
  - Un dossier zip à rendre
pied:
  - "**Crédits des photographies.** Les images `horizon.jpg` et `renard.jpg` proviennent de [Pexels](https://www.pexels.com/) et sont utilisées selon la [licence Pexels](https://www.pexels.com/license/). Photo du renard : Beat Bieri."
---

## Briefing {#presentation .sans-numero}

**Objectif** : apprendre trois transformations de base (redresser, recadrer, réduire les couleurs) et comprendre ce qu'elles changent dans une image.

**Logiciel utilisé** : GIMP 3

**Données fournies** : les images `horizon.jpg` et `renard.jpg`.

**Travail à rendre** : un dossier zip nommé `NOM1_NOM2_retouche_photo` contenant :

- un document Word avec les réponses aux questions ;
- le fichier `NOM1_NOM2_horizon.jpg`, réalisé durant la partie 1 ;
- le fichier `NOM1_NOM2_renard.jpg`, réalisé durant la partie 2 ;
- (bonus) le fichier `NOM1_NOM2_mon_aquarelle.jpg`, réalisé durant le défi.

## Partie 1 : Corriger les défauts d'une image {#partie1 .sans-numero}

Une photo n'est pas toujours parfaite à la sortie de l'appareil. Dans cette partie, tu vas repérer ses défauts, puis les corriger avec deux transformations : redresser et recadrer.

## Repérer les défauts de la photo

Télécharge l'image `horizon.jpg` :

[Télécharger horizon.jpg](ressources/horizon.jpg){.bouton download="horizon.jpg"}

{.aide}
Si l'image s'ouvre dans un onglet au lieu de se télécharger : fais un clic droit sur le bouton, puis <kbd>Enregistrer le lien sous…</kbd>.

Ouvre-la ensuite dans GIMP (_Fichier > Ouvrir_).

**Question 1.** Cette photo a deux défauts. Lesquels ?

**Question 2.** Note les dimensions de l'image en pixels (affichées en bas de la fenêtre, ou dans _Image > Échelle et taille de l'image_) : ……… × ………

## Redresser l'horizon

1. Choisis l'**outil Mesure** dans le menu _Outils > Mesure_ (touche Maj+M).
2. Clique sur un bout de l'horizon, maintiens et tire jusqu'à l'autre bout, puis relâche.
3. Lis l'angle affiché en bas de la fenêtre.
4. Clique sur le bouton **Redresser** dans les options de l'outil (barre verticale à gauche).

**Question 3.** Quel angle as-tu mesuré ?

**Question 4.** Regarde les coins de l'image. Que remarques-tu ? Pourquoi, d'après toi ?

## Recadrer en 16:9

1. Choisis l'**outil Découpage** dans le menu _Outils > Outils de transformation > Découpage_ (Maj+C).
2. Dans les options de l'outil, à gauche, coche la case « Fixé », choisis « Proportions » dans la liste et inscris « 16:9 » dans le champ qui se trouve à la suite. Cela permet de forcer le format 16:9, qui est la norme mondiale pour la télévision HD, les moniteurs ou les plateformes vidéo comme YouTube.
3. Trace un rectangle qui ne contient pas de **zone quadrillée** (ce quadrillage représente la transparence). Tu peux ajuster la taille du rectangle en cliquant sur les coins.
4. Dans les options de l'outil, active les guides **« Règle des tiers »** (clique sur « Aucun guide » pour voir apparaître les options) et place l'horizon sur une des lignes horizontales.
5. Appuie sur **Entrée** pour valider.

**Question 5.** Quelles sont les nouvelles dimensions de l'image ? Quel pourcentage de pixels as-tu perdu ? (Rappel : nombre de pixels = largeur × hauteur)

Exporte le résultat (_Fichier > Exporter sous…_) sous le nom `NOM1_NOM2_horizon.jpg`.

::: cadre
Recadrer, c'est supprimer des pixels, donc la définition diminue. Une règle en photographie de paysage : placer la ligne d'horizon sur le tiers inférieur pour mettre en valeur un beau ciel, ou sur le tiers supérieur pour privilégier le premier plan.
:::

## Partie 2 : Réduire les couleurs pour créer une aquarelle {#partie2 .sans-numero}

Une aquarelle utilise peu de couleurs, en grandes taches douces. Dans cette partie, tu vas réduire le nombre de couleurs d'une photo, comprendre comment le logiciel s'y prend, puis combiner plusieurs réglages pour obtenir un effet d'aquarelle.

## Prédire l'effet de la réduction des couleurs

Télécharge l'image `renard.jpg` :

[Télécharger renard.jpg](ressources/renard.jpg){.bouton download="renard.jpg"}

Ouvre-la ensuite dans GIMP (_Fichier > Ouvrir_). Observe-la bien.

**Question 6.** Quelles sont les 2 couleurs dominantes (les plus présentes) de cette image ?

**Question 7.** On va réduire le nombre de couleurs de cette image. Que va-t-il se passer d'après toi ? Toute l'image sera-t-elle modifiée de la même façon ? Écris ta prédiction en 2 ou 3 lignes.

## Réduire à 32 couleurs

1. _Image > Mode > Couleurs indexées…_
2. Choisis **« Générer une palette optimale »**.
3. Mets le **nombre maximal de couleurs** à **32**.
4. Dans **« Tramage des couleurs »**, choisis **« Aucun »**.
5. Clique sur **Convertir**.

L'image n'utilise désormais que 32 couleurs.

::: cadre
Le logiciel répartit les couleurs de sa palette selon ce qui est le plus présent dans l'image. Tu peux afficher les couleurs utilisées en cliquant sur _Fenêtres > Fenêtres ancrables > Palette_.
:::

Zoome sur différentes zones (Ctrl+molette). Pour comparer avec l'original, utilise _Édition > Annuler_ puis _Édition > Rétablir_.

**Question 8.** Quelles parties/éléments de l'image ont le plus changé ? Quelles parties/éléments de l'image ont le moins changé ?

**Question 9.** D'après toi, à quoi est due cette différence ?

**Question 10.** Décris la forme de ce qui apparaît dans les zones qui ont changé (taille, contours…).

**Question 11.** D'après la palette des couleurs indexées, quelles couleurs sont les plus nombreuses ? Compare avec ta prédiction. Avais-tu vu juste ?

::: cadre
Dans une zone floue, les couleurs changent très doucement d'un pixel à l'autre : c'est un **dégradé**. Dans une zone nette, les couleurs changent beaucoup d'un pixel à l'autre à cause des détails. Pour qu'un dégradé paraisse continu, il faut beaucoup de couleurs intermédiaires, assez proches pour que l'œil ne voie pas où l'une s'arrête et où l'autre commence.
:::

## Choisir le bon nombre de couleurs

::: cadre
Chaque pixel est mémorisé par un nombre. Avec 1 bit on distingue 2 couleurs, avec 2 bits 4 couleurs, etc. Tout à l'heure nous avons demandé 32 couleurs, donc 5 bits (2⁵ = 32).
:::

Teste l'image avec 128, 64 puis 16 couleurs (reviens à l'original entre chaque essai avec _Édition > Annuler Convertir l'image en couleurs indexées_).

**Question 12.** Trouve le plus petit nombre de couleurs pour lequel tu ne vois plus de différence avec l'image d'origine (1) sur le renard, (2) dans le flou du bas. Que remarques-tu ?

**Question 13.** Si tu dois choisir un seul nombre de couleurs pour toute l'image, lequel prends-tu ? Pourquoi ?

## Regrouper les pixels avec Waterpixels

On a vu précédemment qu'en réduisant le nombre de couleurs, des pixels qui avaient des couleurs proches deviennent exactement la même couleur. Dans les zones floues, cela fait apparaître de grandes taches, mais dans les zones texturées, l'effet se voit moins. Une autre méthode consiste à regrouper les pixels qui sont voisins : on découpe l'image en petites zones, et chaque zone prend une seule couleur. C'est ce que fait le filtre Waterpixels.

L'idée : on **regroupe nous-mêmes les pixels voisins sur toute l'image**, avant de réduire de nouveau les couleurs (étape suivante).

1. Reviens à l'image d'origine (ou rouvre `renard.jpg`).
2. Va dans _Filtres > Artistiques > Waterpixels_.
3. Mets la taille des superpixels à 20, laisse le reste par défaut, puis valide.

**Question 14.** Quelles parties/éléments de l'image ont le plus changé ? Quelles parties/éléments de l'image ont le moins changé ?

**Question 15.** Compare avec ce que tu avais obtenu avec la réduction de couleurs.

## Combiner Waterpixels et réduction des couleurs

On a vu précédemment que la réduction du nombre de couleurs fait apparaître des taches dans les zones floues, et que le filtre Waterpixels crée des petites zones de couleur unie dans les zones détaillées. Dans les deux cas, l'image prend un aspect de peinture, mais chaque technique ne travaille que sur un type de zone. On va maintenant combiner les deux techniques.

À partir de l'image précédemment obtenue avec le filtre Waterpixels :

1. _Image > Mode > Couleurs indexées…_
2. Choisis **« Générer une palette optimale »**.
3. Mets le **nombre maximal de couleurs** à **16**.
4. Dans **« Tramage des couleurs »**, choisis **« Aucun »**.
5. Clique sur **Convertir**.

**Question 16.** Observe le résultat. Pourquoi est-il intéressant de combiner les deux méthodes ?

## Adoucir les couleurs (effet pastel)

Ton image a maintenant un aspect de peinture, mais ses couleurs sont encore vives, comme sur la photo d'origine. On veut maintenant s'approcher d'une aquarelle, une peinture à l'eau qui a des couleurs claires et peu intenses. Pour les obtenir, on va utiliser deux réglages qui n'ont rien à voir avec le nombre de couleurs.

1. Ouvre _Couleurs > Teinte-Saturation_.
2. Teste chaque curseur **séparément**, en regardant l'aperçu :
   - **Saturation** vers la gauche (valeurs négatives)
   - **Luminosité** vers la droite (valeurs positives)
3. Règle ensuite les deux ensemble pour obtenir des couleurs pastel (recommandations : saturation entre -30 et -50, luminosité entre +15 et +30).

**Question 17.** Que fait le curseur de **saturation** ? Avant de tester, prédis ce qui se passe à -100, puis vérifie.

**Question 18.** Que fait le curseur de **luminosité** ? Avant de tester, prédis ce qui se passe à +100, puis vérifie.

**Question 19.** Pourquoi faut-il **combiner** les deux réglages pour obtenir un effet pastel ?

Exporte le résultat (_Fichier > Exporter sous…_) sous le nom `NOM1_NOM2_renard.jpg`.

## Créer ta plus belle aquarelle (bonus)

Choisis **ta propre image**. Ton but : obtenir **la plus belle aquarelle possible**.

Tu disposes de quatre réglages : la taille de Waterpixels, la saturation, la luminosité et le nombre de couleurs. Note tes réglages finaux dans ton document Word :

- Taille de Waterpixels : ……
- Saturation : ……
- Luminosité : ……
- Nombre de couleurs : ……

Exporte le résultat sous le nom `NOM1_NOM2_mon_aquarelle.jpg`.
