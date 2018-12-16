import requests

link = "https://api.jikan.moe/v3/top/anime/1/tv"
anime_link = "https://api.jikan.moe/v3/anime/"

resp = requests.get(link)

top = resp.json()['top']
for top_anime in top :
    anime_resp = requests.get(anime_link + str(top_anime['mal_id']))
    print(anime_resp.json())