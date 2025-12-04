import requests
import pandas as pd

BASE_URL = "https://restcountries.com/v3.1"

# 1. Récupérer tous les pays d'Europe
EUROPE_URL = f"{BASE_URL}/region/europe"

european_countries = requests.get(EUROPE_URL).json()

# 2. Créer un DataFrame avec : nom, capitale, population, superficie

data = []

for country in european_countries:
    name = country['name']['common']
    capital = country['capital'][0]
    population = country['population']
    area = country['area']
    languages = country['languages'].values()
    data.append({
        'name' : name,
        'capital' : capital,
        'population' : population, 
        'superficie' : area, 
        'languages' :  list(languages) 
    })

df = pd.DataFrame(data)

# 3. Calculer la densité de population (population / superficie)

df['densite'] = df['population'] / df['superficie']

print(df)

# 4. Identifier les 5 pays les plus peuplés d'Europe

print("# 5 pays les plus peuplés d'Europe")
top_five_countries = df.nlargest(5, 'population')
print(top_five_countries)

# 5. Calculer la population totale de l'Europe

print("# Population totale de l'Europe")
total_population = df["population"].sum()
print(total_population)

# 6. Trouver le pays avec la plus grande densité

print("# Pays avec la plus grande densité")
country_with_largest_population = df.nlargest(1, "densite")
print(country_with_largest_population)



# Bonus 

top_three_languages = df.explode("languages").groupby("languages")["languages"].count().nlargest()
print(top_three_languages.to_dict())

european_languages = df.explode("languages").groupby("languages")["population"].sum()

data = []
for key, value in top_three_languages.to_dict().items():
    langues = key 
    nb_countries = value
    population = european_languages.to_dict()[key]
    data.append({
        'langues' : langues,
        'Nombre de pays' : nb_countries, 
        'Population concernée' : population
    })


df2 = pd.DataFrame(data)

# Sauvegarder les résultats dans `pays_europe.xlsx`

with pd.ExcelWriter('./pays_europe.xlsx') as writer:
    df.to_excel(writer, sheet_name='Europe', index=False)
    df2.to_excel(writer, sheet_name='Languages', index=False)