import requests
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df=0, stop_words='english')

link = "https://api.jikan.moe/v3/top/anime/1/tv"
anime_link = "https://api.jikan.moe/v3/anime/"
user_link = "https://api.jikan.moe/v3/user/Frost_Master/animelist/all" # change user name here

resp = requests.get(link)

animes = [[]]

# create dataset
top = resp.json()['top']
for top_anime in top :
    anime_resp = requests.get(anime_link + str(top_anime['mal_id']))
    genres_str = ""
    for genres in anime_resp.json()['genres']:
        genres_str = genres_str + genres['name'] + "|"
    genres_str = genres_str[:-1] #TODO this is gay fix this
    animes.append([str(top_anime['title']), genres_str, 1])

resp = requests.get(user_link)
users_anime = resp.json()['anime']
user_anime_names = []

for user_anime in users_anime:
    anime_resp = requests.get(anime_link + str(user_anime['mal_id']))
    genres_str = ""
    for genres in anime_resp.json()['genres']:
        genres_str = genres_str + genres['name'] + "|"
    genres_str = genres_str[:-1]  # TODO this is gay fix this
    animes.append([str(user_anime['title']), genres_str, 0])
    user_anime_names.append([str(user_anime['title'])])

# DATASET IS DONE OMG

frame = pd.DataFrame(data=animes[1:],
                     columns=['title', 'genres', 'fromTop20'])

tfidf_matrix = tf.fit_transform(frame['genres'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

titles = frame['title']
indices = pd.Series(frame.index, index=frame['title'])


idx = indices['One Punch Man'] # PUT TITLE HERE
sim_scores = list(enumerate(cosine_sim[idx]))
sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
sim_scores = sim_scores[1:21]
movie_indices = [i[0] for i in sim_scores]

recommended_animes = titles.iloc[movie_indices]

for anime in recommended_animes:
    if str(anime) not in str(user_anime_names):
        print(str(anime))
        break
