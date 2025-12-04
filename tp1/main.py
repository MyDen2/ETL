import pandas as pd
import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]
dfs = []
for f in files:
    if f.startswith("magasin_"):
        name = "df_" + f.split('.')[0]
        name = pd.read_csv(f)
        name['magasin'] = f.split("magasin_")[1].split('.')[0]
        dfs.append(name)
        print(name)

# 1. 
# df_A = pd.read_csv('./magasin_A.csv')
# print(df_A)

# df_B = pd.read_csv('./magasin_B.csv')
# print(df_B)

# df_C = pd.read_csv('./magasin_C.csv')
# print(df_C)

result = pd.concat(dfs)


# 2

# df_A['magasin'] = "A"
# print(df_A)
# df_B['magasin'] = "B"
# print(df_B)
# df_C['magasin'] = "C"
# print(df_C)

# 3.

print("\n--- Concaténation verticale (ignore_index=True) ---")
df_concat_all = pd.concat(dfs, ignore_index=True)
print(df_concat_all) 

# 4 

print("\n--- Suppression des doublons---")
df_concat_all = df_concat_all.drop_duplicates()
print(df_concat_all)

#5

df_concat_all['montant_total'] = df_concat_all['quantite'] * df_concat_all['prix_unitaire']
print(df_concat_all)

#6

df_par_magasin = df_concat_all.groupby('magasin')['montant_total'].sum()
df_par_vendeur = df_concat_all.groupby(['magasin', 'vendeur'])['montant_total'].sum()
df_top_produits = df_concat_all.groupby('produit')['quantite'].sum().sort_values(ascending=False).head(10)

print("\n--- Rapport excel ---")
with pd.ExcelWriter('rapport.xlsx') as writer:
    df_concat_all.to_excel(writer, sheet_name='Consolidé', index=False)
    df_par_magasin.to_excel(writer, sheet_name='Par magasin')
    df_par_vendeur.to_excel(writer, sheet_name='Par vendeur')
    df_top_produits.to_excel(writer, sheet_name='Top produits')
