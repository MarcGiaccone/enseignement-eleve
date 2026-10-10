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

Chaque activité est un sous-dossier numéroté contenant `tp.md` et `ressources/`, par exemple `seconde-snt/01-metadonnees/`.

## Ajouter une activité

1. Créer `<niveau>/NN-titre-court/tp.md` et `<niveau>/NN-titre-court/ressources/`.
2. Écrire le déroulé en Markdown : voir [outils/README.md](outils/README.md).
3. Commit et push : la page est générée et publiée automatiquement.

Les pages d'accueil et les pages de niveau sont générées aussi : il n'y a rien à y ajouter à la main.
