#!/usr/bin/python3

inventaire = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
]

inventaire_inverse = [(quantite, fruit) for fruit, quantite in inventaire]

# Avec la fonction sorted
inventaire_inverse_trie = [(fruit, quantite) for quantite, fruit in sorted(inventaire_inverse, reverse=True)]
print(inventaire_inverse_trie)

# Avec la methode sort
inventaire_inverse.sort(reverse=True)
inventaire_inverse_trie = [(fruit, quantite) for quantite, fruit in inventaire_inverse]
print(inventaire_inverse_trie)
