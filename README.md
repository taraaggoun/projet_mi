# PROJET MATHS-INFO 2023 : Factorisation des grands nombres

## Sommaire

1. [Introduction et informations](README.md#introduction-et-informations)
2. [Compilation et Exection du projet](README.md#compilation-et-execution-du-projet)

----------------------------------------------------------------------

## Introduction et informations

Le système de Cryptographie RSA est basé sur le fait qu’il est très simple de multiplier deux nombres
entiers, alors qu’il est extrêmement difficile de retrouver les deux facteurs si on ne connaît que le
produit. Dans ce projet, on étudiera des méthodes pour factoriser des nombres. On verra également
quelques tests de primalité, qui permettent de détecter si un nombre est premier sans avoir à
montrer explicitement qu’il ne possède aucun diviseur non trivial.

**Identifiants et membres du groupe**

|  Name   | First name    | Student number |
|:-------:|:-------------:|:--------------:|
| Aggoun  |     Tara      |    21961069    |
|  Aziz   |   Ghizlane    |    21965976    |

----------------------------------------------------------------------

## Compilation et Execution du projet

**Compilation/Execution**

Pour executer le projet, il suffit d'entrer la commande suivante :

```
python3 Main.py [ *nom_de_l_algo* ] [ *nombre_a_factoriser* ]
```
*Le nom de l'algorithme et le nombre à factoriser sont optionels.*

*Si le nom de l'algorithme n'est pas donné, l'algorithme de division successive ser lancé*

*Si le nombre à factoriser n'est pas donné, un nombre aléatoire qui a deux facteur premier compris entre 2¨15 et 2¨20 sera géneré*

*Pour modifier les borne du générateur, modifier **min** et **max** et pour le nombre de facteur, modifier **n** dans la fonction **generator** du fichier `algorithmes/util/generator.py`*

Pour généré un graphe, des trois algorithmes, du temps de factorisation d'un nombre en fonction de sa taille.
Entrer les commandes suivante:

```
cd graphe
```

```
python3 graphe
```

**Algorithme implementé**
- `DS` :			Division successive
- `Fermat` :		Fermat
- `Kraitchik` :		Kraitchik

----------------------------------------------------------------------