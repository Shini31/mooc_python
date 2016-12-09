#!/usr/bin/python3

inventaire = {"pommes": 22,
              "melons": 4,
              "poires": 18,
              "fraises": 76,
              "prunes": 51
              }

# Avec la fonction sorted
inventaire_trie = sorted(inventaire.items(), key=lambda x: x[1])
print(inventaire_trie)
