# Outils de Calculs Mécaniques

Ce dépôt contient une collection de scripts Python pour différents calculs mécaniques. Ces outils sont conçus pour aider les ingénieurs et étudiants dans leurs calculs courants.

## Scripts disponibles

### 1. Poutre d'Euler-Bernoulli (`poutre_euler_bernoulli.py`)
- Calcul de la flèche d'une poutre
- Calcul des contraintes
- Visualisation de la déformation
- Basé sur la théorie des poutres d'Euler-Bernoulli

### 2. Système Bielle-Manivelle (`bielle_manivelle.py`)
- Analyse cinématique complète
- Calcul des vitesses
- Calcul des accélérations
- Visualisation des mouvements

### 3. Dimensionnement d'Arbre (`dimensionnement_arbre.py`)
- Calcul du diamètre minimal
- Vérification des contraintes
- Prise en compte du coefficient de sécurité

## Prérequis
```bash
pip install numpy matplotlib
```

## Utilisation

Chaque script peut être exécuté individuellement :
```bash
python poutre_euler_bernoulli.py
python bielle_manivelle.py
python dimensionnement_arbre.py
```

## Exemples d'utilisation

### Poutre d'Euler-Bernoulli
```python
poutre = PoutreEulerBernoulli(L=2.0, E=210e9, I=(0.05 * 0.1**3)/12, q=1000)
poutre.plot_fleche()
```

### Bielle-Manivelle
```python
mecanisme = BielleManivelle(L_manivelle=0.05, L_bielle=0.2, omega=50)
mecanisme.plot_cinematique()
```

### Dimensionnement d'Arbre
```python
arbre = DimensionnementArbre(couple=1000, limite_elastique=400e6)
diametre = arbre.diametre_minimal()
```

## Contribution
N'hésitez pas à contribuer à ce projet en soumettant des pull requests ou en signalant des problèmes dans la section Issues.
