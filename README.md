# Enseignement — version élève (public)

Cours, TD et TP pour les élèves. Ce dépôt est **public** : il ne doit contenir aucun corrigé ni donnée personnelle. Les corrigés sont dans le dépôt privé `enseignement-prof`.

Le site est généré à partir des fichiers Markdown et publié avec GitHub Pages à chaque push. Les élèves ouvrent simplement le lien d'une activité, sans compte.

## Arborescence

```
assets/             gabarit visuel commun (tp.css, tp.js)
outils/             script de génération, modèles HTML, guide d'écriture
seconde-snt/        SNT, seconde
premiere-sti2d/     STI2D, première
terminale-sti2d/    STI2D, terminale
```

Chaque niveau est découpé en thèmes (`seconde-snt/photo-numerique/`). Chaque activité est un sous-dossier numéroté dans son thème, contenant `tp.md` et `ressources/`, par exemple `seconde-snt/photo-numerique/02-metadonnees/`. La numérotation `NN` repart à 01 dans chaque thème.

## Ajouter une activité

1. Si le thème est nouveau, le déclarer dans `outils/niveaux.yml` (sinon le build refuse le TP).
2. Créer `<niveau>/<thème>/NN-titre-court/tp.md` et `<niveau>/<thème>/NN-titre-court/ressources/`.
3. Écrire le déroulé en Markdown : voir [outils/README.md](outils/README.md).
4. Commit et push : la page est générée et publiée automatiquement.

Les pages d'accueil et les pages de niveau sont générées aussi : il n'y a rien à y ajouter à la main.
