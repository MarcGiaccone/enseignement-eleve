# Écrire un TP en Markdown

Un TP = un dossier avec un fichier `tp.md` et un dossier `ressources/`. À chaque push, la CI (`.github/workflows/pages.yml`) génère les pages avec `outils/build.py` et les publie sur GitHub Pages.

```
seconde-snt/02-titre-court/
├── tp.md             le déroulé
└── ressources/       images, pages HTML, tout ce qui sert à faire le TP
```

Le dossier `ressources/` est copié tel quel (les images ne sont pas retouchées, leurs métadonnées sont conservées). Une page HTML de `ressources/` appelle le gabarit par `../../../assets/tp.css`.

## Prévisualiser sur son PC

```bash
pip install -r outils/requirements.txt
python outils/build.py
```

Le site est généré dans `_site/` (ignoré par git). Pour le voir avec ses liens : `python -m http.server --directory _site`, puis http://localhost:8000. Le script s'arrête avec une erreur si un lien ou une image pointe vers un fichier qui n'existe pas.

## En-tête du `tp.md`

```yaml
---
titre: Que dit une photo de vous ?
titre_page: "TP SNT : que dit une photo de vous ?"   # facultatif, titre de l'onglet
surtitre: SNT · Seconde · Travaux pratiques
intro: "Phrase d'accroche sous le titre."             # facultatif
detail: "Phrase affichée sur la carte du niveau."     # facultatif, sinon la liste « meta »
meta:                                                  # pastilles sous le titre
  - 1 h 30
  - En binôme
pied:                                                  # paragraphes du pied de page (Markdown en ligne)
  - "**Crédits.** ..."
---
```

Les valeurs qui contiennent `:` doivent être entre guillemets.

## Corps du TP

| Pour obtenir | Écrire |
|---|---|
| Une étape numérotée | `## Titre {duree="15 minutes"}` |
| Une étape sans numéro | `## Titre {.sans-numero}` |
| Un identifiant d'ancre précis | `## Titre {#e3 duree="…"}` (sinon `e1`, `e2`…) |
| Un sous-titre | `### Titre` |
| Une question | un paragraphe qui commence par `**Q7.**` ou `**Question 7.**` |
| Un encadré d'alerte | `::: alerte` … `:::` |
| Un encadré d'information | `::: cadre` … `:::` |
| Un indice repliable | `::: indice Texte du bouton` … `:::` (sans texte : « Indice ») |
| Une photo avec légende | `![description](ressources/images/a.jpg "Légende")` seul sur sa ligne |
| Un bouton de téléchargement | `[Télécharger](ressources/images/a.jpg){.bouton download="a.jpg"}` |
| Un bouton secondaire | `{.bouton .secondaire …}` |
| Un bouton qui ouvre un nouvel onglet | `[Ouvrir](ressources/x.html){.bouton target="_blank" rel="noopener"}` |
| Une petite note d'aide | une ligne `{.aide}` juste avant le paragraphe |
| Une touche de clavier | `<kbd>Entrée</kbd>` |
| Un tableau | tableau Markdown ; la première cellule vide de chaque ligne est mise en forme comme case à remplir |

Le plan en haut de page est construit automatiquement à partir des titres `##`. Les liens `http(s)://` s'ouvrent dans un nouvel onglet.

## Modifier l'apparence

- Le style de tous les TP est dans `assets/tp.css`.
- La structure d'un TP (en-tête, plan, pied de page) est dans `outils/modele-tp.html`, celle des pages d'accueil dans `outils/modele-index.html`.
- La liste des niveaux est dans `outils/niveaux.yml`.

Une modification de ces fichiers change toutes les pages au prochain build.
