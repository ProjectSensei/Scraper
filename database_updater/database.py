import sys
import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import cursor

load_dotenv()

anime_db = mysql.connector.connect(
    host = os.getenv("HOST"),
    user = os.getenv("USER"),
    password = os.getenv("PASSWORD"),
    database = os.getenv("DATABASE"),
    port = os.getenv("PORT")
)

db_cursor = anime_db.cursor()

# Insert anime data in anime_database table with columns having anime name and episodes in from of JSON
def insert_anime(name, episodes):
    sql = "INSERT INTO anime_database (name, episodes) VALUES (%s, %s)"
    val = (name, episodes)
    db_cursor.execute(sql, val)
    anime_db.commit()

# Clears all the data inside anime_database table
def truncate_table():
    sql = "TRUNCATE anime_database"
    db_cursor.execute(sql)


if __name__ == "__main__":
    argument = sys.argv[1]
    if argument == "--truncate":
        truncate_table()
        print("[+] Table has been truncated")
