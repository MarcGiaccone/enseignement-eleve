#!/usr/bin/env python3
"""Génère le site des TP à partir des fichiers tp.md.

Pour chaque <niveau>/<activité>/tp.md, produit <activité>/index.html avec le
modèle outils/modele-tp.html, copie ressources/ à l'identique, puis génère les
pages d'accueil. Le résultat est écrit dans le dossier donné par --out.

Usage : python outils/build.py [--out _site]
"""
import argparse
import html
import re
import shutil
import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markdown_it import MarkdownIt
from markdown_it.token import Token
from mdit_py_plugins.attrs import attrs_block_plugin, attrs_plugin
from mdit_py_plugins.container import container_plugin

RACINE = Path(__file__).resolve().parent.parent
OUTILS = Path(__file__).resolve().parent

ATTRS_FIN = re.compile(r"\s*\{([^{}]*)\}\s*$")
ATTR_ELEMENT = re.compile(r'(#[\w-]+|\.[\w-]+|[\w-]+="[^"]*"|[\w-]+=\S+)')
NUM_QUESTION = re.compile(r"Q(\d+)\.")
LIEN_EXTERNE = ("http://", "https://", "mailto:", "tel:", "#", "data:")


class ErreurTP(Exception):
    pass


def lire_attrs(texte):
    """Lit « #id .classe cle="valeur" » ; renvoie (id, classes, valeurs)."""
    ident, classes, valeurs = None, [], {}
    for element in ATTR_ELEMENT.findall(texte):
        if element[0] == "#":
            ident = element[1:]
        elif element[0] == ".":
            classes.append(element[1:])
        else:
            cle, valeur = element.split("=", 1)
            valeurs[cle] = valeur.strip('"')
    return ident, classes, valeurs


def slug(texte):
    texte = re.sub(r"[^\w\s-]", "", texte.lower())
    return re.sub(r"[\s_]+", "-", texte).strip("-") or "etape"


def creer_markdown():
    md = MarkdownIt("commonmark", {"html": True}).enable("table")
    md.use(attrs_plugin).use(attrs_block_plugin)

    def div(classes):
        def rendre(self, tokens, idx, options, env):
            return f'<div class="{classes}">\n' if tokens[idx].nesting == 1 else "</div>\n"
        return rendre

    def indice(self, tokens, idx, options, env):
        jeton = tokens[idx]
        if jeton.nesting == -1:
            return "</details>\n"
        resume = jeton.info.strip().removeprefix("indice").strip() or "Indice"
        return f"<details>\n<summary>{html.escape(resume)}</summary>\n"

    md.use(container_plugin, name="alerte", render=div("cadre alerte"))
    md.use(container_plugin, name="cadre", render=div("cadre"))
    md.use(container_plugin, name="indice", render=indice)

    def ouvrir_etape(self, tokens, idx, options, env):
        jeton = tokens[idx]
        if jeton.tag != "h2":
            return self.renderToken(tokens, idx, options, env)
        env["courante"] = jeton.meta
        sortie = "</section>\n" if env.get("ouverte") else ""
        env["ouverte"] = True
        numero = jeton.meta["numero"]
        pastille = f'<span class="numero">{numero}</span> ' if numero else ""
        return f'{sortie}<section class="etape" id="{jeton.meta["id"]}">\n<h2>{pastille}'

    def fermer_etape(self, tokens, idx, options, env):
        if tokens[idx].tag != "h2":
            return self.renderToken(tokens, idx, options, env)
        duree = env["courante"]["duree"]
        suite = f'<p class="duree">{html.escape(duree)}</p>\n' if duree else ""
        return "</h2>\n" + suite

    md.add_render_rule("heading_open", ouvrir_etape)
    md.add_render_rule("heading_close", fermer_etape)
    return md


def marquer_lien_externe(jeton):
    """Les liens http(s) s'ouvrent dans un nouvel onglet."""
    if jeton.type == "link_open" and jeton.attrs.get("href", "").startswith(("http://", "https://")):
        jeton.attrs.setdefault("target", "_blank")
        jeton.attrs.setdefault("rel", "noopener")


def rendre_inline(md, texte):
    """Markdown en ligne (intro, pied de page) rendu avec les mêmes règles de liens."""
    enfants = md.parseInline(texte, {})[0].children
    for enfant in enfants:
        marquer_lien_externe(enfant)
    return md.renderer.renderInline(enfants, md.options, {})


def preparer(md, jetons, env, dossier):
    """Annote les jetons (étapes, questions, figures, tableaux, liens)."""
    etapes, questions = [], []
    numero = 0
    dans_tbody = False
    ids = set()

    for i, jeton in enumerate(jetons):
        if jeton.type == "heading_open" and jeton.tag == "h2":
            inline = jetons[i + 1]
            fin = ATTRS_FIN.search(inline.content)
            ident, classes, valeurs = lire_attrs(fin.group(1)) if fin else (None, [], {})
            if fin:
                inline.content = inline.content[: fin.start()]
                inline.children = md.parseInline(inline.content, env)[0].children
            numerote = "sans-numero" not in classes
            if numerote:
                numero += 1
            ident = ident or (f"e{numero}" if numerote else slug(inline.content))
            if ident in ids:
                raise ErreurTP(f"identifiant d'étape en double : {ident}")
            ids.add(ident)
            jeton.meta = {"id": ident, "duree": valeurs.get("duree"), "numero": numero if numerote else None}
            titre = md.renderer.renderInline(inline.children, md.options, env)
            etapes.append({"id": ident, "titre": titre})

        elif jeton.type == "paragraph_open" and not jeton.hidden:
            inline = jetons[i + 1]
            tous = inline.children or []
            enfants = [e for e in tous if not (e.type == "text" and e.content == "")]
            if (len(enfants) >= 3 and enfants[0].type == "strong_open"
                    and enfants[2].type == "strong_close"
                    and NUM_QUESTION.fullmatch(enfants[1].content)):
                jeton.attrJoin("class", "q")
                questions.append(int(NUM_QUESTION.fullmatch(enfants[1].content).group(1)))
            elif len(enfants) == 1 and enfants[0].type == "image":
                jeton.tag = "figure"
                jeton.attrSet("class", "photo")
                jetons[i + 2].tag = "figure"
                legende = enfants[0].attrs.pop("title", None)
                if legende:
                    tous.append(Token("html_inline", "", 0, content=f"<figcaption>{html.escape(legende)}</figcaption>"))

        elif jeton.type == "tbody_open":
            dans_tbody = True
        elif jeton.type == "tbody_close":
            dans_tbody = False
        elif jeton.type == "tr_open" and dans_tbody:
            deja = False
            j = i + 1
            while jetons[j].type != "tr_close":
                if jetons[j].type == "td_open" and not deja and jetons[j + 1].content.strip() == "":
                    jetons[j].attrJoin("class", "vide")
                    deja = True
                j += 1

        elif jeton.type == "inline":
            for enfant in jeton.children or []:
                marquer_lien_externe(enfant)
                if enfant.type in ("link_open", "image"):
                    cible = enfant.attrs.get("href") or enfant.attrs.get("src", "")
                    if cible and not cible.startswith(LIEN_EXTERNE):
                        chemin = dossier / cible.split("#")[0].split("?")[0]
                        if not chemin.exists():
                            raise ErreurTP(f"fichier introuvable : {cible}")

    return etapes, questions


def lire_tp(chemin):
    texte = chemin.read_text(encoding="utf-8")
    if not texte.startswith("---\n"):
        raise ErreurTP("en-tête YAML manquant (le fichier doit commencer par ---)")
    entete, _, corps = texte[4:].partition("\n---\n")
    donnees = yaml.safe_load(entete) or {}
    for cle in ("titre", "surtitre"):
        if not donnees.get(cle):
            raise ErreurTP(f"champ « {cle} » manquant dans l'en-tête")
    return donnees, corps


def generer_activite(md, env_jinja, chemin_tp, racine_sortie):
    dossier = chemin_tp.parent
    donnees, corps = lire_tp(chemin_tp)
    env = {}
    jetons = md.parse(corps, env)
    etapes, questions = preparer(md, jetons, env, dossier)
    if questions != list(range(1, len(questions) + 1)):
        print(f"  attention : numérotation des questions inhabituelle {questions}", file=sys.stderr)
    html_corps = md.renderer.render(jetons, md.options, env)
    if env.get("ouverte"):
        html_corps += "</section>\n"

    rel = dossier.relative_to(RACINE)
    assets = "../" * len(rel.parts) + "assets/"
    page = env_jinja.get_template("modele-tp.html").render(
        titre=donnees.get("titre_page") or donnees["titre"],
        titre_h1=donnees["titre"],
        surtitre=donnees["surtitre"],
        intro=rendre_inline(md, donnees.get("intro", "")),
        meta=donnees.get("meta", []),
        pied=[rendre_inline(md, p) for p in donnees.get("pied", [])],
        plan=etapes,
        corps=html_corps,
        assets=assets,
    )
    sortie = racine_sortie / rel
    sortie.mkdir(parents=True, exist_ok=True)
    (sortie / "index.html").write_text(page, encoding="utf-8", newline="\n")
    if (dossier / "ressources").is_dir():
        shutil.copytree(dossier / "ressources", sortie / "ressources", dirs_exist_ok=True)
    detail = donnees.get("detail") or " · ".join(donnees.get("meta", []))
    return {"href": dossier.name + "/", "titre": f"{dossier.name.split('-')[0]} — {donnees['titre']}", "detail": detail}


def ecrire_index(env_jinja, chemin, assets, titre, intro, cartes, retour=None):
    chemin.parent.mkdir(parents=True, exist_ok=True)
    page = env_jinja.get_template("modele-index.html").render(
        titre=titre, intro=intro, cartes=cartes, assets=assets, retour=retour)
    chemin.write_text(page, encoding="utf-8", newline="\n")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    parseur = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parseur.add_argument("--out", default="_site", help="dossier de sortie (défaut : _site)")
    sortie = Path(parseur.parse_args().out).resolve()
    if sortie == RACINE or sortie in RACINE.parents:
        sys.exit("--out ne peut pas être la racine du dépôt ni un de ses parents")

    if sortie.exists():
        shutil.rmtree(sortie)
    sortie.mkdir(parents=True)
    shutil.copytree(RACINE / "assets", sortie / "assets")

    config = yaml.safe_load((OUTILS / "niveaux.yml").read_text(encoding="utf-8"))
    md = creer_markdown()
    env_jinja = Environment(loader=FileSystemLoader(OUTILS), autoescape=select_autoescape(["html"]),
                            trim_blocks=True, lstrip_blocks=True)

    erreurs = 0
    cartes_niveaux = []
    for niveau in config["niveaux"]:
        cartes = []
        for chemin_tp in sorted((RACINE / niveau["dossier"]).glob("*/tp.md")):
            print(f"{chemin_tp.relative_to(RACINE)}")
            try:
                cartes.append(generer_activite(md, env_jinja, chemin_tp, sortie))
            except ErreurTP as e:
                erreurs += 1
                print(f"  ERREUR : {e}", file=sys.stderr)
        ecrire_index(env_jinja, sortie / niveau["dossier"] / "index.html", "../assets/",
                     niveau["titre"], niveau.get("detail", ""), cartes, retour="../")
        cartes_niveaux.append({"href": niveau["dossier"] + "/", "titre": niveau["titre"], "detail": niveau.get("detail", "")})
    ecrire_index(env_jinja, sortie / "index.html", "assets/", config["titre"], config.get("intro", ""), cartes_niveaux)

    if erreurs:
        sys.exit(f"{erreurs} erreur(s) : le site n'est pas fiable.")
    print(f"Site généré dans {sortie}")


if __name__ == "__main__":
    main()
