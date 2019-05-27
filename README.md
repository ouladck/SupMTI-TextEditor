# SupMTI-TextEditor

Un éditer de texte fait en utilisant PyGTK.
C'est mon mini-projet de cours Python pour l'école SupMTI Rabat.

![Screen](./assets/supmti-texteditor.png?s=500x200)

## C'est quoi ce Python?

Python est un langage de programmation interprété, multi-paradigme et multiplateformes. Il favorise la programmation impérative structurée, fonctionnelle et orientée objet. Il est doté d'un typage dynamique fort, d'une gestion automatique de la mémoire par ramasse-miettes et d'un système de gestion d'exceptions ; il est ainsi similaire à Perl, Ruby, Scheme, Smalltalk et Tcl.

## Et GTK?

GTK (The GIMP Toolkit, anciennement GTK+3) est un ensemble de bibliothèques logicielles, c'est-à-dire un ensemble de fonctions permettant de réaliser des interfaces graphiques. Cette bibliothèque a été développée originellement pour les besoins du logiciel de traitement d'images GIMP. GTK+ est maintenant utilisé dans de nombreux projets, dont les environnements de bureau GNOME, Xfce, Lxde et ROX.

GTK est un projet libre (licence GNU LGPL 2.1) et multiplate-forme.

# Fonctionnalités

## Coloration syntaxique (Hightlight Syntax)

![Hightlight](./assets/hightlight.png)
>Example un code en PHP

L'utilisation de `GtkSourceView` pour l'implémentation de la coloration syntaxique dans l'éditeur.
Les langues supportées :
C, C++, Java, C#, Fortran, sh, Javascript, Python, Perl, Ruby, PHP, TCL, XML, HTML, DocBook, LaTeX, ...

## Recherche

![Recherche](./assets/search.png)
> Rechercher le mot `file`

![Recherche](./assets/find.png)
> Couloriser les mots `file` trouvé

## Rechercher et replacé

![Recherche](./assets/replace.png)
> Rechercher le mot `file`

![Recherche](./assets/replaced.png)
> le replacer par le mot `fichier`

## Multi-langage

Utilisation de `gettext` pour l'internationalisation de l'application.
`SupMti TextEditor` est disponible en Arabe, Français et Anglais.


# Raccourcis

| Action  | Raccourci |
| ------------- | ------------- |
| Sauvgarder  | `CTL` + `s`  |
| Rechercher  | `CTL` + `f`  |
| Replacer  | `CTL` + `r`  |
| Quiter  | `CTL` + `q`  |
| Ouvrir  | `CTL` + `o`  |
