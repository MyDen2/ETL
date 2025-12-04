import pandas as pd

# 1. Charger les données avec Pandas
df = pd.read_excel('ventes_janvier.xlsx')
print(df)


# - Supprimer les doublons

print("\n--- Suppression des doublons---")
df = df.drop_duplicates()
print(df)

# - Remplir les valeurs manquantes de `region` par "Non spécifié"

print("\n--- Remplir les valeurs manquantes de `region` par \"Non spécifié\" ---")
df['region'] = df['region'].fillna("Non spécifié")
print(df) 

# - Convertir `date` en datetime

df['date'] = pd.to_datetime(df['date'])

# # 3 - - Créer `montant_total` = quantite × prix_unitaire

df['montant_total'] = df['quantite'] * df['prix_unitaire']
print(df)

# - Extraire le `jour` et `jour_semaine` de la date
df['date'] = pd.to_datetime(df['date'])
df['jour'] = df['date'].dt.dayofweek
df['jour_semaine'] = df['date'].dt.day_name()
print(df)

# - Total des ventes par région

total_ventes_par_region = df.groupby("region")["montant_total"].sum()
print(f"Montant total par region : {total_ventes_par_region}")

# - Produit le plus vendu (en quantité)

produit_le_plus_vendu = df.groupby("produit")["quantite"].sum().nlargest(1)
print(f"Produit le plus vendu (en quantité) : {produit_le_plus_vendu}")
df_par_region = df.groupby("produit")['quantite'].sum()

# - Jour de la semaine avec le plus de ventes

jour_semaine_avec_le_plus_ventes = df.groupby("jour_semaine")["quantite"].sum().nlargest(1)
print(f"Jour de la semaine avec le plus de ventes : {jour_semaine_avec_le_plus_ventes}")
df_par_produit = df.groupby("jour_semaine")['quantite'].sum()
# sunday

# - Feuille "Données" : Données nettoyées 

# Plusieurs feuilles dans le même fichier
print("\n--- Écriture dans plusieurs feuilles (multi_sheets.xlsx) ---")
with pd.ExcelWriter('ventes_analysees.xlsx') as writer:
    df.to_excel(writer, sheet_name='Données', index=False)
    df_par_region.to_excel(writer, sheet_name='Par région')
    df_par_produit.to_excel(writer, sheet_name='Par produit')
