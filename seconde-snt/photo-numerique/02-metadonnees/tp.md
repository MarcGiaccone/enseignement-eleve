---
titre: Que dit une photo de vous ?
titre_page: "TP SNT : que dit une photo de vous ?"
surtitre: SNT · Seconde · Travaux pratiques
intro: "Une seule photo, quelques clics, et une personne se retrouve identifiée. Vous allez le vérifier sur un cas fictif, puis comprendre comment l'éviter."
meta:
  - 1 h 30
  - En binôme
  - Poste Windows + navigateur
  - Feuille de notes à rendre
pied:
  - "**Situation fictive.** Le personnage, le réseau Courseo, le club et les résultats sportifs sont inventés pour ce TP. Toute ressemblance avec une personne réelle est fortuite. Les métadonnées des deux images ont été écrites pour l'occasion."
  - "**Crédits des photographies.** Les deux photographies proviennent de Wikimedia Commons et sont diffusées sous licence [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.fr). Photo n° 1 : Txllxt TxllxT. Photo n° 2 : Valentinois26. Les images ont été redimensionnées, leurs métadonnées d'origine ont été supprimées et remplacées par des métadonnées fictives pour ce TP. Les images modifiées restent sous la même licence."
  - "**Programme.** SNT (Seconde) : thèmes « La photographie numérique », « Localisation, cartographie et mobilité » et « Les réseaux sociaux »."
---

## Mission et règles {#mission .sans-numero}

Une photo vient d'être publiée sur **Courseo**, un réseau social inventé pour ce TP.

Vous êtes une équipe de sensibilisation. À partir de cette seule photo, vous allez retrouver tout ce que vous pouvez sur la personne qui l'a publiée, puis lui expliquer comment elle aurait pu se protéger.

::: alerte
**Règle absolue**

Le personnage, le réseau Courseo, le club et la course sont **entièrement inventés**. Vous enquêtez uniquement sur ce personnage fictif. Vous ne cherchez jamais d'informations sur une vraie personne : ni un camarade, ni un professeur, ni une célébrité.
:::

### Ce qu'il vous faut

- un ordinateur Windows avec un navigateur ;
- le site **[exiftools.com](https://exiftools.com/)**, qui sert à lire les informations cachées dans une photo (il faut une connexion internet) ;
- une feuille à part pour vos réponses.

### Votre feuille de notes

Vous répondez aux questions numérotées (**Q1**, **Q2**, etc.) sur une feuille à part, avec les noms des deux membres du binôme. Écrivez le numéro de la question devant chaque réponse. La feuille sera ramassée et notée en fin de séance.

## Le pari {duree="5 minutes · pas de logiciel pour l'instant"}

Voici la photo publiée sur Courseo.

![Photographie d'une allée d'arbres bordée de bancs, avec une tour au fond et un ciel bleu](ressources/images/photo_1.jpg "Photo n° 1, publiée sur Courseo.")

[Télécharger la photo n° 1](ressources/images/photo_1.jpg){.bouton download="photo_1.jpg"}

{.aide}
Si l'image s'ouvre dans un onglet au lieu de se télécharger : faites un clic droit sur l'image, puis <kbd>Enregistrer l'image sous…</kbd>, et enregistrez-la dans un dossier `TP_SNT` de vos documents (créez-le si besoin).

::: alerte
N'utilisez **ni capture d'écran ni copier-coller** : les informations cachées dans la photo seraient perdues.
:::

### Le pari

Sans ouvrir aucun logiciel, recopiez ce tableau sur votre feuille et remplissez-le en 3 minutes. Une réponse incertaine vaut mieux qu'une case vide. Notez votre **confiance** de 0 (au hasard) à 10 (certain).

| Question | Votre pari | Confiance (0 à 10) | Ce qui vous fait dire ça |
|---|---|---|---|
| **Où** la photo a-t-elle été prise ? (ville, quartier) | | | |
| **Quand** ? (saison, jour de la semaine, heure) | | | |
| **Qui** l'a prise ? (nom, âge, métier) | | | |

**Q1.** Recopiez et remplissez le tableau du pari.

**Q2.** Quelle ligne a votre confiance la plus basse ? Que vous manquerait-il pour en être sûrs ?

## Lire les métadonnées {duree="20 minutes"}

Un fichier photo ne contient pas seulement des pixels. L'appareil y écrit aussi, automatiquement, des informations cachées : les **métadonnées** (format **EXIF**). On y trouve la date, le modèle de téléphone, la position GPS, et parfois le nom de l'auteur.

Windows en affiche une partie, mais on ne peut pas les copier. Vous allez donc utiliser le site **[exiftools.com](https://exiftools.com/)**, qui les affiche toutes.

### Ouvrir la photo dans exiftools.com

1. Ouvrez **[exiftools.com](https://exiftools.com/)** dans un nouvel onglet.
2. Glissez `photo_1.jpg` depuis votre dossier `TP_SNT` dans la zone **Upload files** (ou cliquez dans la zone et choisissez le fichier).
3. Le site affiche d'abord un résumé. Plus bas, sous **Full Metadata**, cliquez sur <kbd>Expand All</kbd> puis ouvrez la rubrique **EXIF** : toutes les métadonnées s'affichent, avec des noms en anglais.

::: alerte
En envoyant une photo sur ce site, vous la confiez à un service extérieur. Ici, aucun souci : la photo du TP est sous licence libre. **Ne le faites jamais avec une photo de vous ou de vos proches.**
:::

::: cadre
Ne confondez pas la date de prise de vue avec la **date de modification du fichier** (`FileModifyDate`). Cette dernière dépend de votre ordinateur, pas de l'appareil photo.
:::

### Relever les informations

Recopiez ce tableau sur votre feuille et complétez-le **uniquement** avec ce que vous trouvez dans la rubrique EXIF du site. Écrivez « rien » quand un champ n'existe pas.

| Information | Nom en anglais dans l'outil | Valeur trouvée |
|---|---|---|
| Date et heure de prise de vue | `DateTimeOriginal` | |
| Marque du téléphone | `Make` | |
| Modèle du téléphone | `Model` | |
| Auteur | `Artist` | |
| Copyright | `Copyright` | |
| Titre | `XPTitle` | |
| Commentaire | `XPComment` | |
| Latitude | `GPSLatitude` | |
| Longitude | `GPSLongitude` | |

::: indice Indice : je ne trouve pas un champ
La liste est longue et classée par groupes (EXIF, Composite, File...). Si vous ne voyez que quelques lignes, cliquez sur <kbd>Expand All</kbd> pour afficher **toutes** les informations de la rubrique EXIF.

Les noms sont en anglais et collés : `Artist` veut dire auteur. Un champ vide n'apparaît pas dans la liste : notez « rien ».
:::

### Questions

**Q3.** Quel jour de la semaine correspond à la date de prise de vue ? (Aidez-vous d'un calendrier.) Quelle heure était-il ? Que faisait probablement la personne à ce moment-là ?

**Q4.** Reprenez votre pari de l'étape 1, lignes **Quand** et **Qui**. Qu'est-ce qui était juste ? Qu'est-ce que les métadonnées vous apprennent que l'image seule ne disait pas ?

**Q5.** Quel champ vous donne un premier moyen de retrouver la personne qui a pris la photo ?

## Localiser {duree="15 minutes"}

Les champs `GPSLatitude` et `GPSLongitude` donnent la position exacte de l'appareil au moment de la photo. Inutile de les recopier : le site les place directement sur une carte.

1. Gardez `photo_1.jpg` ouverte sur exiftools.com.
2. Dans le résumé, repérez la carte **GPS Location** : un repère indique où la photo a été prise. Le site affiche aussi les coordonnées et l'adresse la plus proche.
3. Zoomez sur la carte jusqu'à reconnaître les bâtiments et les rues.

::: indice Indice : je ne vois pas la carte
Copiez la position dans Google Maps :

1. Relevez dans la rubrique EXIF les champs `GPSLatitude`, `GPSLatitudeRef`, `GPSLongitude` et `GPSLongitudeRef`.
2. Ouvrez [Google Maps](https://www.google.com/maps) dans un nouvel onglet.
3. Dans la barre de recherche, tapez la latitude puis la longitude, avec `°` à la place de `deg` et une lettre à la place du mot : `N` (North), `S` (South), `E` (East), `W` (West). Exemple : `48°51'29.6"N 2°17'40.2"E`.
:::

### Questions

**Q6.** Zoomez au maximum autour du repère. Où la photo a-t-elle été prise ? Répondez en une phrase : la ville, et le type d'endroit (parc, rue, place, cour d'immeuble...).

**Q7.** Ce lieu est-il public ou privé ? Cela change-t-il le risque de publier cette photo ?

**Q8.** Dans la rubrique EXIF, repérez `GPSLatitude` et `GPSLongitude`, puis les champs `GPSLatitudeRef` et `GPSLongitudeRef` qui les accompagnent. Lequel des deux nombres indique la position nord-sud, lequel la position est-ouest ? Que vous apprennent les deux champs `Ref` ?

::: indice
La **latitude** mesure la distance à l'équateur, vers le nord (N) ou le sud (S). La **longitude** mesure la distance au méridien de Greenwich, vers l'est (E) ou l'ouest (W).
:::

**Q9.** Le GPS d'un téléphone est précis à quelques mètres. Cette position suffit-elle pour savoir où la personne habite ? Qu'est-ce qu'elle prouve avec certitude, et qu'est-ce qu'elle ne prouve pas ?

## Recouper les informations {duree="25 minutes"}

Une information seule est souvent banale. Ce qui devient dangereux, c'est de **croiser** plusieurs sources. Votre point de départ : le pseudo que vous avez trouvé à l'étape 2.

[Ouvrir le réseau Courseo (fictif)](ressources/courseo.html){.bouton target="_blank" rel="noopener"}

**Q10.** Retrouvez le profil de l'auteur de la photo n° 1 (tapez son pseudo dans la recherche, avec les chiffres et les tirets du bas). Qu'apprenez-vous sur la personne : prénom, âge, ville, activités, habitudes ?

**Q11.** Son nom de famille n'apparaît pas sur son profil, mais une de ses publications vous donne une piste. Retrouvez-le. Quel chemin avez-vous suivi ?

**Q12.** La photo n° 1 est-elle cohérente avec ce que raconte le profil (jour, heure, lieu) ? Citez deux éléments.

### La deuxième photo

Une autre photo a été publiée plus tard.

![Seconde photographie : un kiosque à musique sur une esplanade, dans une lumière rasante](ressources/images/photo_2.jpg "Photo n° 2.")

[Télécharger la photo n° 2](ressources/images/photo_2.jpg){.bouton .secondaire download="photo_2.jpg"}

{.aide}
Même méthode qu'à l'étape 1 si le téléchargement ne démarre pas. Envoyez-la ensuite sur exiftools.com de la même façon et regardez sa carte.

**Q13.** Cette photo n'a pas d'auteur dans ses métadonnées. Comment pouvez-vous pourtant être presque certains qu'elle vient de la même personne ? Donnez au moins deux éléments.

::: indice
Comparez avec la photo n° 1 : le modèle de téléphone, la version du logiciel, la position sur la carte, et la publication correspondante sur Courseo.
:::

**Q14.** Que vous apprend cette deuxième photo sur les habitudes de la personne ?

**Q15.** La publication qui accompagne cette photo dit que la personne habite « à 5 minutes à pied » du lieu. Sur la carte, estimez la zone où elle habite. Pourriez-vous trouver son adresse exacte avec ces seules informations ? Et si elle publiait d'autres informations plus tard ?

::: indice
Un adulte marche environ 5 km/h. Combien de mètres parcourt-il en 5 minutes ? Utilisez l'échelle de la carte pour tracer ce rayon autour du lieu.
:::

## Effacer les traces {duree="5 minutes"}

Heureusement, on peut nettoyer une photo avant de la partager.

1. Faites une **copie** de `photo_1.jpg` dans le même dossier (clic droit, copier, coller). Ne travaillez jamais sur votre seul exemplaire.
2. Clic droit sur la copie, <kbd>Propriétés</kbd>, onglet <kbd>Détails</kbd>, puis le lien en bas <kbd>Supprimer les propriétés et les informations personnelles</kbd>.
3. Choisissez <kbd>Créer une copie avec toutes les propriétés possibles supprimées</kbd>, puis <kbd>OK</kbd>.
4. Revenez sur exiftools.com, cliquez sur <kbd>Clear All</kbd> pour vider la liste, puis envoyez la nouvelle copie.

**Q16.** Qu'est-ce qui a disparu des métadonnées ? Qu'est-ce qui reste ?

::: cadre
Ce nettoyage protège seulement **cette** copie. Un fichier déjà envoyé reste intact chez son destinataire. Une photo envoyée en « qualité originale » par e-mail ou messagerie garde en général ses métadonnées. Certains réseaux sociaux les retirent à la publication, mais ce n'est pas une règle générale. Et rien n'efface ce que l'image montre elle-même : un lieu reconnaissable, une personne.
:::

## Bilan à rendre {duree="15 minutes"}

**Q17.** Sur votre feuille, reproduisez et complétez ce tableau avec toutes les informations que vous avez pu apprendre sur le personnage (au moins six lignes).

| Information retrouvée | D'où elle vient<br><small>(image, métadonnée, profil, autre page)</small> | Pourquoi c'est un risque |
|---|---|---|
| | | |
| | | |
| | | |

Puis répondez en quelques phrases.

**Q18.** Aucune de ces informations n'est secrète à elle seule. Pourquoi, **mises ensemble**, permettent-elles d'identifier quelqu'un ?

**Q19.** Quelles erreurs le personnage a-t-il commises ? Écrivez trois gestes concrets qu'il aurait dû faire pour se protéger.

**Q20.** Quelles conséquences possibles pour lui, et pour ses proches ?

::: cadre
**Pour finir, sans rien montrer à personne.** Regardez dans les réglages de l'appareil photo de votre téléphone si la localisation est activée. Ce que vous y trouvez ne sera pas ramassé.
:::
