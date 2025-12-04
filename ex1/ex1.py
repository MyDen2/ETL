import pandas as pd
import csv

df = pd.read_csv("ventes.csv")

# **Tâches**
# 1. Charger le fichier avec Pandas
df = pd.read_csv("ventes.csv")
print(df)

# 2. Ajouter une colonne `montant_total` (quantite × prix_unitaire)
print("# 2. Ajouter une colonne `montant_total` (quantite × prix_unitaire)")
df["montant_total"] = df["quantite"] * df["prix_unitaire"]
print(df)

# 3. Calculer le total des ventes par vendeur
print("# 3. Calculer le total des ventes par vendeur")
total_ventes_par_vendeur = df.groupby("vendeur")["montant_total"].sum()
print(total_ventes_par_vendeur)

# 4. Calculer le total des ventes par produit

print("# 4. Calculer le total des ventes par produit")
total_ventes_par_produit = df.groupby("produit")["quantite"].sum()
print(total_ventes_par_produit)

# 5. Identifier le top 3 des ventes (montant le plus élevé)

print("# 5. Identifier le top 3 des ventes (montant le plus élevé)")
top_trois_ventes = df.sort_values("montant_total", ascending=False).head(3)
print(top_trois_ventes)

print("v2")
top_trois_ventes_v2 = df.nlargest(3, 'montant_total')
print(top_trois_ventes_v2)

# 6. Sauvegarder les résultats dans `ventes_analysees.csv`

df.to_csv("ventes_analysees.csv", index = False)

# Bonus 

with open("rapport.txt", "w") as f:
    f.write(f"1. Calculer le total des ventes par vendeur : \n {total_ventes_par_vendeur} \n")
    f.write(f"2. Calculer le total des ventes par produit : \n {total_ventes_par_produit} \n")
    f.write(f"3. Identifier le top 3 des ventes (montant le plus élevé) : \n {top_trois_ventes} \n")

 