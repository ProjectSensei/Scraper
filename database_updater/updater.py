import json
from database import insert_anime

# Loading anime data file
anime_data_file = open("anime_data.json")
anime_data = json.load(anime_data_file) 

# Uploading anime data, one anime at a time to the database
completed = 0
for anime_name in anime_data:
    player_links = json.dumps(anime_data[anime_name])
    print(f"[*] [{completed + 1} / {len(anime_data)}] Inserting {anime_name} to anime_database")
    insert_anime(anime_name, player_links)
    completed += 1