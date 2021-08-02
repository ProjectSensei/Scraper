# Scraper

### Dataabse Updater
The script `updater.py` in `./database_updater` is responsible for pushing all the data inside `anime_data.json` to the MySQL `anime_database` table.

`python updater.py` - `updater.py` scripts starts pushing anime data from `anime_data.json` to the database, one anime at a time.
`python database.py --truncate`  - Deletes all the anime entries from anime database table so that you can do a fresh upload using `updater.py`
