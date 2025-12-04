import requests
import pandas as pd


BASE_URL = 'https://jsonplaceholder.typicode.com'


# 1. Récupérer tous les utilisateurs (`/users`)
users = requests.get(f"{BASE_URL}/users").json()

# 2. Afficher le nom et l'email de chaque utilisateur
for user in users:
    print(f"{user['name']} {user['email']}")


# 3. Récupérer tous les posts de l'utilisateur avec `userId=1`
posts_user1 = requests.get(f"{BASE_URL}/posts",params={'userId' : 1}).json()
print(f"Nombre de post de l'user avec id 1 : {len(posts_user1)}")

# 4. Compter combien de posts chaque utilisateur a créé
all_posts = requests.get(f"{BASE_URL}/posts").json()
posts_par_user = {}
for post in all_posts:
    user_id = post['userId']
    posts_par_user[user_id] = posts_par_user.get(user_id,0) + 1
print("Postes par user : ",posts_par_user)

# 5. Récupérer les commentaires du post `id=1`
comments = requests.get(f"{BASE_URL}/posts/1/comments").json()
print(f"Nombre de commentaires du post avec l'id 1 : {len(comments)} ")

# 6. Créer un DataFrame Pandas avec :
#    - Colonnes : post_id, post_title, nombre_commentaires
#    - Pour les 10 premiers posts
#    - enregistrer ce dataframe en csv

data = []
for post in all_posts[:10]:
    post_id = post['id']
    post_title = post['title']
    # recup du nb de commentaires
    nb_comments = len(requests.get(f"{BASE_URL}/posts/{post_id}/comments").json())
    data.append({
        'post_id' : post_id,
        'post_title' : post_title,
        'nombre_commentaires' : nb_comments
    })

print(data)

df = pd.DataFrame(data)

print("DATA en dataframe :")
print(df)

df.to_csv('output.csv',index=False)